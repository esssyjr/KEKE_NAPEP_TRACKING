# KEKE_NAPEP_TRACKING
## Overview

This project builds upon a previously model I developed for keke_napep (tricycle) detection [KEKE_NAPEP_Detection Model](https://github.com/esssyjr/KEKE_NAPEP_DETECTION/tree/main).
We used this pre-trained model to implement KENE_NAPEP_TRACKING model, crucial for traffic management and other applications in Nigeria.
### Tracking Implementation
The tracking system in this repository captures video, uses the custom detection model to identify Keke Napep in each frame, and tracks the 
detected objects across frames, providing real-time tracking information. Using the Supervision library from Roboflow, a tool commonly used for computer vision tasks, the 
detection model is implemented for tracking. The performance is very good and up to standard. However, it may have shortfalls depending on the type of data used for tracking,
as the effectiveness heavily relies on the initial data used for implementing the detection model.

## Future Improvements

This tracking model has the potential to be extended for various applications beyond basic tracking, like:

### Speed Estimation:
By incorporating information from multiple frames (e.g., frame rate, distance traveled between frames), you can estimate the speed of tracked keke napeps.
### Counting: 
Implement a counter to track the total number of unique keke napeps that appear in the video. This might involve maintaining track IDs and ensuring proper track 
termination and creation.
## Collaboration
As a computer vision model developer, I acknowledge my limitations and recognize the importance of collaboration in making projects a reality. While I bring expertise in
developing models and algorithms, I understand that collaborative efforts can enhance the scope and impact of projects.

I am open to collaboration on this project and others, leveraging the collective expertise of diverse individuals to overcome challenges and achieve shared goals. Whether 
you're a fellow developer, data scientist, software developer, domain expert, or enthusiast, I welcome collaboration opportunities to push the boundaries of AI applications.

If you're interested in collaborating or have ideas for potential projects, feel free to reach out.
## Citation
The dataset utilized in this project was provided by EJAZTECH.AI, a company dedicated to gathering local datasets for AI applications, founded by me. We acknowledge their 
invaluable contribution to the development of this model and other models by providing access to diverse and localized data, which played a crucial role in developing
the KEKE_NAPEP_TRACKING model. I express my gratitude to EJAZTECH.AI for their commitment to advancing AI research and applications in Nigeria and beyond.

For further inquiries or collaboration opportunities, you can contact the company via their email address:

Email: [ejaztech.ai@gmail.com]

