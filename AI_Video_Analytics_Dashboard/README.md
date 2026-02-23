# AI Video Analytics Dashboard
# 📊 AI Video Analytics Dashboard

An AI-powered real-time video analytics dashboard built using Python, OpenCV, YOLOv8, and Streamlit.

This system performs live object detection (humans and vehicles), logs detection events, and visualizes analytics such as detections per minute through an interactive web dashboard.

Designed for:
- AI & Computer Vision learning
- Smart monitoring systems
- Engineering mini/major projects
- Portfolio and placement preparation

---

## 🚀 Features

- Real-time object detection
- Detects: person, car, bus, truck, motorcycle
- Live detection count display
- CSV-based event logging
- Analytics graph (detections per minute)
- Streamlit web-based dashboard
- Works with webcam or video file
- Fully offline after first model download

---

## 🧠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- Streamlit
- Pandas
- Matplotlib

---

## 📂 Project Structure

AI_Video_Analytics_Dashboard/
│
├── app.py
├── detector.py
├── config.py
├── requirements.txt
├── logs/
├── captures/
└── README.md

---

## ⚙️ Installation

1. Install Python 3.10 or later.
2. Clone the repository:

   git clone <your-repository-link>

3. Navigate to project folder:

   cd AI_Video_Analytics_Dashboard

4. Install dependencies:

   pip install -r requirements.txt

5. Run the dashboard:

   streamlit run app.py

The YOLOv8 model will automatically download on first execution.

---

## 📈 How It Works

1. Video stream is captured from webcam or file.
2. YOLOv8 detects target objects in each frame.
3. Detection events are:
   - Counted in real-time
   - Logged in CSV format
4. Dashboard displays:
   - Total object count
   - Detections per minute graph

---

## 🖥 System Requirements

Minimum:
- Windows 11
- 8GB RAM
- Webcam

Recommended:
- NVIDIA GPU for faster inference

---

## ⚠️ Current Limitation

This version uses frame-based detection counting.
If the same object remains in frame, it may increase the count multiple times.

Future versions can include:
- Object tracking (DeepSORT)
- Line-crossing accurate counting
- Multiple analytics charts
- Real-time FPS monitoring
- Dark mode UI
- Cloud database integration

---

## 🔒 Ethical Notice

This project is intended for educational and research use only. Ensure compliance with privacy and data protection laws before real-world deployment.

---

## 👨‍💻 Author

Developed as an AI-based video analytics project.

Real-time AI-based object detection dashboard using YOLOv8, OpenCV, and Streamlit.

## Features
- Live video monitoring
- Human & vehicle detection
- Real-time object count
- CSV logging of detections
- Analytics graph (detections per minute)
- Streamlit web dashboard

## Setup

1. Install Python 3.10+
2. Install dependencies:
   pip install -r requirements.txt
3. Run the dashboard:
   streamlit run app.py

YOLO model will auto-download on first run.
