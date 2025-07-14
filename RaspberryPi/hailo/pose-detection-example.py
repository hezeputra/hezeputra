import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib
import os
import numpy as np
import cv2
import hailo
import threading
import time
import io

from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, StreamingResponse
import uvicorn

from hailo_apps.hailo_app_python.core.common.buffer_utils import get_caps_from_pad, get_numpy_from_buffer
from hailo_apps.hailo_app_python.core.gstreamer.gstreamer_app import app_callback_class
from hailo_apps.hailo_app_python.apps.pose_estimation.pose_estimation_pipeline import GStreamerPoseEstimationApp

# -----------------------------------------------------------------------------------------------
# Global Setup
# -----------------------------------------------------------------------------------------------
app_fastapi = FastAPI()
user_data = None  # will be initialized later

# Skeleton pairs for drawing lines between keypoints
POSE_SKELETON = [
    ('left_shoulder', 'right_shoulder'),
    ('left_shoulder', 'left_elbow'),
    ('left_elbow', 'left_wrist'),
    ('right_shoulder', 'right_elbow'),
    ('right_elbow', 'right_wrist'),
    ('left_shoulder', 'left_hip'),
    ('right_shoulder', 'right_hip'),
    ('left_hip', 'right_hip'),
    ('left_hip', 'left_knee'),
    ('left_knee', 'left_ankle'),
    ('right_hip', 'right_knee'),
    ('right_knee', 'right_ankle'),
    ('nose', 'left_eye'),
    ('nose', 'right_eye'),
    ('left_eye', 'left_ear'),
    ('right_eye', 'right_ear'),
]

# -----------------------------------------------------------------------------------------------
# User-defined class
# -----------------------------------------------------------------------------------------------
class user_app_callback_class(app_callback_class):
    def __init__(self):
        super().__init__()
        self.keypoints_data = None

    def set_pose_data(self, frame, keypoints):
        self.set_frame(frame)
        self.keypoints_data = keypoints

    def get_pose_data(self):
        return self.get_frame(), self.keypoints_data

# -----------------------------------------------------------------------------------------------
# Callback function
# -----------------------------------------------------------------------------------------------
def app_callback(pad, info, user_data):
    buffer = info.get_buffer()
    if buffer is None:
        return Gst.PadProbeReturn.OK

    format, width, height = get_caps_from_pad(pad)
    frame = None
    keypoints_list = []

    if user_data.use_frame and format and width and height:
        frame = get_numpy_from_buffer(buffer, format, width, height)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        roi = hailo.get_roi_from_buffer(buffer)
        detections = roi.get_objects_typed(hailo.HAILO_DETECTION)
        keypoints_map = get_keypoints()

        for detection in detections:
            if detection.get_label() != "person":
                continue

            bbox = detection.get_bbox()
            landmarks = detection.get_objects_typed(hailo.HAILO_LANDMARKS)
            if not landmarks:
                continue

            points = landmarks[0].get_points()
            keypoint_entry = {}

            for name, index in keypoints_map.items():
                pt = points[index]
                x = int((pt.x() * bbox.width() + bbox.xmin()) * width)
                y = int((pt.y() * bbox.height() + bbox.ymin()) * height)
                keypoint_entry[name] = {"x": x, "y": y}
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)  # Draw keypoint

            # Draw bounding box
            x1 = int(bbox.xmin() * width)
            y1 = int(bbox.ymin() * height)
            x2 = int((bbox.xmin() + bbox.width()) * width)
            y2 = int((bbox.ymin() + bbox.height()) * height)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # Draw skeleton
            for pair in POSE_SKELETON:
                if pair[0] in keypoint_entry and pair[1] in keypoint_entry:
                    pt1 = (keypoint_entry[pair[0]]['x'], keypoint_entry[pair[0]]['y'])
                    pt2 = (keypoint_entry[pair[1]]['x'], keypoint_entry[pair[1]]['y'])
                    cv2.line(frame, pt1, pt2, (0, 255, 255), 2)

            keypoints_list.append(keypoint_entry)

    if frame is not None:
        user_data.set_pose_data(frame, keypoints_list)

    return Gst.PadProbeReturn.OK

def get_keypoints():
    return {
        'nose': 0, 'left_eye': 1, 'right_eye': 2, 'left_ear': 3, 'right_ear': 4,
        'left_shoulder': 5, 'right_shoulder': 6, 'left_elbow': 7, 'right_elbow': 8,
        'left_wrist': 9, 'right_wrist': 10, 'left_hip': 11, 'right_hip': 12,
        'left_knee': 13, 'right_knee': 14, 'left_ankle': 15, 'right_ankle': 16,
    }

# -----------------------------------------------------------------------------------------------
# FastAPI routes
# -----------------------------------------------------------------------------------------------
@app_fastapi.get("/")
def index():
    html = """
    <html>
        <head><title>Live Pose Stream</title></head>
        <body>
            <h1>Live Pose Estimation</h1>
            <img src="/video" width="854" height="480" />
        </body>
    </html>
    """
    return HTMLResponse(content=html)

@app_fastapi.get("/pose")
def start_pose():
    return JSONResponse(content={"status": "Pipeline already running."})

@app_fastapi.get("/video")
def video_feed():
    def generate():
        while True:
            frame, keypoints_data = user_data.get_pose_data()
            if frame is not None:
                ret, jpeg = cv2.imencode(".jpg", frame)
                if ret:
                    yield (b"--frame\r\n"
                           b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")
            time.sleep(0.03)  # ~30 FPS
    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace; boundary=frame")

# -----------------------------------------------------------------------------------------------
# Start FastAPI and GStreamer app
# -----------------------------------------------------------------------------------------------
def start_api():
    uvicorn.run(app_fastapi, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    # Start FastAPI in background
    api_thread = threading.Thread(target=start_api, daemon=True)
    api_thread.start()

    # Start pipeline in main thread
    user_data = user_app_callback_class()
    app_instance = GStreamerPoseEstimationApp(app_callback, user_data)
    app_instance.run()