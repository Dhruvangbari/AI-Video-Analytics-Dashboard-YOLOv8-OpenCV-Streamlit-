import streamlit as st
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
from detector import detect
from config import VIDEO_SOURCE

st.title("AI Video Analytics Dashboard")

os.makedirs("logs", exist_ok=True)

cap = cv2.VideoCapture(VIDEO_SOURCE)

frame_placeholder = st.empty()
count_placeholder = st.empty()

log_file = "logs/analytics_log.csv"

if not os.path.exists(log_file):
    pd.DataFrame(columns=["timestamp", "label"]).to_csv(log_file, index=False)

vehicle_count = 0

if st.button("Start Monitoring"):
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detect(frame)

        for label, conf, x1, y1, x2, y2 in detections:
            vehicle_count += 1

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{label}", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            pd.DataFrame([[datetime.datetime.now(), label]],
                         columns=["timestamp", "label"]).to_csv(
                log_file, mode='a', header=False, index=False)

        frame_placeholder.image(frame, channels="BGR")
        count_placeholder.write(f"Total Objects Detected: {vehicle_count}")

cap.release()

st.header("Analytics")

if os.path.exists(log_file):
    data = pd.read_csv(log_file)
    if not data.empty:
        data["timestamp"] = pd.to_datetime(data["timestamp"])
        data["minute"] = data["timestamp"].dt.strftime("%H:%M")
        count_per_min = data.groupby("minute").size()

        fig = plt.figure()
        plt.plot(count_per_min.index, count_per_min.values)
        plt.xticks(rotation=45)
        plt.xlabel("Time (Minute)")
        plt.ylabel("Detections")
        plt.title("Detections Per Minute")
        st.pyplot(fig)
