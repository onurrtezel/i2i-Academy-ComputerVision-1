# i2i Academy - Computer Vision

This repository contains the solution for the i2i Academy Computer Vision assignment.

## Objectives
1. Understand the fundamentals of Computer Vision (CV).
2. Process live camera feed frame-by-frame using OpenCV.
3. Implement real-time hand-tracking and coordinate extraction using MediaPipe.
4. Apply algorithmic logic to detect finger states (open/closed) and count fingers.

## Theoretical Knowledge

* **Question 1: What is Computer Vision, and what are its primary use cases in the modern tech industry?**
  **Answer: Computer Vision is a field of artificial intelligence that enables computers to interpret and understand visual information from digital images or videos. In the modern tech industry, its primary use cases include autonomous vehicles, medical image analysis, facial recognition, and automated quality control in manufacturing.**

* **Question 2: What is the key difference between image classification and object detection?**
  **Answer: While image classification identifies the primary category or label of an entire image, object detection identifies and locates multiple specific objects within that image, drawing bounding boxes around them.**

* **Question 3: Why do software engineers often prefer using pre-trained frameworks (like MediaPipe) instead of training a custom neural network from scratch for simple tracking tasks?**
  **Answer: Software engineers prefer pre-trained frameworks because they offer optimized, production-ready models that save significant time and computation resources. These frameworks provide high-accuracy real-time tracking out of the box, eliminating the need to collect, label, and train on massive datasets.**

## How It Works
The script captures webcam frames and passes them to MediaPipe's hand tracking model. The status of each finger is calculated as follows:
- **Thumb:** The x-coordinate of the thumb tip (landmark 4) is compared to the joint below it (landmark 3), dynamically adjusting based on whether it is a left or right hand.
- **Other 4 Fingers:** The y-coordinate of each finger tip (landmarks 8, 12, 16, 20) is compared to its corresponding lower joint (landmarks 6, 10, 14, 18). If the tip is higher on screen (lower y-value), it is counted as open.

## Installation & Execution

### 1. Install Dependencies
```bash
pip install opencv-python mediapipe
```

### 2. Run the Application
```bash
python main.py
```
*Press `q` inside the video window to quit.*
