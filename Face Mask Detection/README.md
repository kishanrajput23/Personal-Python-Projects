# Face Mask Detection 😷

## What is this?
A computer vision project that detects whether people in an image or video stream are wearing face masks. It demonstrates face detection, simple classification (mask/no-mask), and drawing bounding boxes with labels on detected faces.

## How it works
- The script uses OpenCV for image/video capture and face detection (Haar cascades or DNN).
- For mask classification it either applies a pre-trained classifier model (e.g., a small CNN) or a simple heuristic classifier included in the project.
- Detected faces are annotated on the frame with a colored box and a label indicating `Mask` or `No Mask`.

**Main script(s):** `Face Mask Detection using openCV.py`

### Requirements
- Python 3.x
- opencv-python (install: `pip install opencv-python`)
- (Optional) tensorflow/keras if a neural model is included

### How to run
1. Install dependencies: `pip install opencv-python`
2. Place any provided model files in the project folder (if applicable).
3. Run: `python "Face Mask Detection using openCV.py"`
4. For camera input, allow access to the webcam when prompted; for images, modify the script to process local image files.

## Summary
This project is a hands-on example for applying OpenCV to real-world safety applications. It can be extended with a more accurate classifier, dataset collection/augmentation, or integration into an alerting system.

