# 🎯 YOLO Real-Time Object Detection

A real-time object detection project built using **Python, YOLO (You Only Look Once), and OpenCV**. This project uses a webcam to detect and identify objects in live video streams with bounding boxes and confidence scores.

## 📌 Project Overview

This project demonstrates how computer vision and deep learning can be used to identify objects in real time.

The YOLO model processes webcam frames and detects objects such as people, cars, mobile phones, laptops, animals, and other common objects.

The project is designed for beginners who want to explore AI, machine learning, and computer vision.

## 🚀 Features

- Real-time object detection using a webcam
- YOLOv8 deep learning model
- Object identification with labels
- Bounding boxes around detected objects
- Confidence score filtering
- Live video processing using OpenCV
- Simple and beginner-friendly Python implementation

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| YOLOv8 | Object detection model |
| Ultralytics | YOLO model implementation |
| OpenCV | Webcam access and video processing |
| NumPy | Numerical operations |

## 📂 Project Structure

```text
object_detection/
│
├── mood_detection.py    # Main Python program
├── yolov8n.pt           # YOLO model weights (downloaded automatically)
└── README.md            # Project documentation
```

## ⚙️ Installation

### 1. Install Python

Install Python 3.12 from the official website:

https://www.python.org/downloads/

Verify your Python installation:

```bash
python --version
```

Expected output:

```text
Python 3.12.x
```

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate to the project directory:

```bash
cd YOUR_REPOSITORY
```

### 3. Install Required Libraries

```bash
python -m pip install ultralytics opencv-python
```

### 4. Run the Project

```bash
python mood_detection.py
```

The program will open your webcam and begin detecting objects in real time.

Press **Q** to close the detection window.

## 🧠 How It Works

1. The program loads the pretrained YOLOv8 Nano model.
2. OpenCV captures video frames from the webcam.
3. YOLO processes each frame and identifies objects.
4. Bounding boxes and labels are drawn around detected objects.
5. The processed video is displayed in a live window.

## 📸 Example Output

The application displays a live webcam feed with detected objects.

Example detections:

```text
Person       Confidence: 0.92
Cell Phone   Confidence: 0.87
Laptop       Confidence: 0.95
Bottle       Confidence: 0.89
```

*Confidence scores are illustrative and may vary depending on the image and model.*

## 📦 YOLO Model

This project uses:

**YOLOv8 Nano (`yolov8n.pt`)**

The Nano model is lightweight and suitable for real-time inference on many computers.

The model is automatically downloaded by Ultralytics when it is first used, if it is not already available locally.

## 🔮 Future Improvements

- Facial emotion detection (happy, sad, angry, neutral)
- Object tracking
- Detection of custom-trained objects
- FPS counter
- Video file processing
- Save detection results
- Build a graphical user interface (GUI)

## ⚠️ Important Note

This project performs general object detection.

Detecting human emotions such as happiness, sadness, anger, or fear requires a separate facial emotion recognition model. Object detection alone does not determine a person's mood.

## 👩‍💻 Author

**Abida Khanam**

AI Student | Karakoram International University (KIU), Gilgit

Interested in Artificial Intelligence, Machine Learning, Deep Learning, and Computer Vision.

## 📄 License

This project is intended for educational and research purposes.

You may modify and improve the project for your own learning and development.
