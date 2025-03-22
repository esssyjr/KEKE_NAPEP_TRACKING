import gradio as gr
import numpy as np
import cv2
from PIL import Image
from ultralytics import YOLO

# Load the YOLO plant detection model
keke_model = YOLO('KEKE_NAPEP.pt')

# Function to detect plants and draw red bounding boxes (plant detection)
def detect_keke(image):
    results = keke_model(image, 0.3)  # YOLO processes the image directly
    image_np = np.array(image)
    
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()  # Get bounding box coordinates
        labels = result.boxes.cls.cpu().numpy()  # Get the predicted class indices
        confs = result.boxes.conf.cpu().numpy()  # Get confidence scores
        
        for box, label, conf in zip(boxes, labels, confs):
            xmin, ymin, xmax, ymax = map(int, box)
            # Draw a red bounding box with thicker lines
            cv2.rectangle(image_np, (xmin, ymin), (xmax, ymax), (0, 0, 255), 4)  # Red color, thickness 4
            class_name = keke_model.names[int(label)]  # Get the class name
            text = f"{class_name} {conf:.2f}"
            # Put class label and confidence score above the bounding box
            cv2.putText(image_np, text, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    
    # Convert the result back to a PIL image for display in Gradio
    output_image = Image.fromarray(image_np)
    return output_image

# Create the Gradio interface for plant detection
interface = gr.Interface(
    fn=detect_keke,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(label="Keke_Napep Detection"),
    title="Keke_Napep Detection System"
)

interface.launch(share=True)
