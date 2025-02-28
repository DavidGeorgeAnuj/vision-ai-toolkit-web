from flask import Flask, render_template, request, jsonify, Response
import cv2
import os
import numpy as np
from ultralytics import YOLO
import easyocr
import shutil

app = Flask(__name__)

# ----- Configuration -----
UPLOAD_FOLDER = "uploads"
GALLERY_FOLDER = "Gallery"
MATCH_THRESHOLD = 0.5

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GALLERY_FOLDER, exist_ok=True)

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

running = False  # Controls real-time detection
stop_flag = False  # Stop signal for detection
video_path = None  # Stores uploaded video path

@app.route("/")
def home():
    return render_template("index.html")

# Initialize EasyOCR reader globally
reader = easyocr.Reader(['en', 'hi'])

@app.route("/text_recognition", methods=["POST"])
def text_recognition():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save uploaded file temporarily
    temp_path = os.path.join(UPLOAD_FOLDER, "temp_image.jpg")
    file.save(temp_path)

    # Ensure the file is saved
    if not os.path.exists(temp_path):
        return jsonify({"error": "File saving failed"}), 500

    # Extract text
    extracted_text = imagetotext(temp_path)

    # Remove temp file
    os.remove(temp_path)

    return jsonify({"text": extracted_text})

def imagetotext(image_path):
    # Read image properly
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if image is None:
        return ["Error: Image could not be loaded"]

    # Convert to grayscale (optional, improves OCR in some cases)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use EasyOCR
    result = reader.readtext(gray)
    return [text[1] for text in result]  # Extract only the text part


@app.route("/realtime_detection")
def realtime_detection():
    """Starts real-time object detection and streams it to the web UI."""
    global running, stop_flag
    running = True
    stop_flag = False
    return Response(generate_webcam_feed(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/upload_video", methods=["POST"])
def upload_video():
    """Uploads video and streams the detection output."""
    global video_path, stop_flag
    stop_flag = False
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    video_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(video_path)
    return jsonify({"status": "Video uploaded", "stream_url": "/video_feed"}), 200

@app.route("/video_feed")
def video_feed():
    """Streams object detection on the uploaded video."""
    return Response(generate_video_feed(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/stop_detection", methods=["POST"])
def stop_detection():
    global running, stop_flag
    stop_flag = True  # Ensure stop signal is properly set
    running = False  # Stop all active processing
    return jsonify({"status": "stopped"}), 200





def detect_objects(frame):
    """Runs YOLOv8 object detection on a frame."""
    results = model(frame)
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box
        confidence = float(box.conf[0])  # Confidence
        class_name = model.names[int(box.cls[0])]  # Class name
        
        # Draw bounding box & label
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.putText(frame, f"{class_name} {confidence:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

def generate_webcam_feed():
    """Captures webcam frames and processes them for object detection."""
    global running, stop_flag
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    while cap.isOpened():
        if stop_flag:  # Exit the loop when stop is requested
            break

        if not ret:
            break

        frame = detect_objects(frame)

        # Encode frame to JPEG
        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

    cap.release()
def generate_video_feed():
    """Processes uploaded video and streams detected output."""
    global video_path, stop_flag
    if not video_path:
        return
    
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened() and not stop_flag:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detect_objects(frame)

        # Encode frame to JPEG
        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

    cap.release()


if __name__ == "__main__":
    app.run(debug=True)
