from flask import Flask, render_template, Response, redirect, url_for
from ultralytics import YOLO
import cv2
import threading
import numpy as np
from flask import jsonify

app = Flask(__name__)
model = YOLO("best.pt")  # Pastikan best.pt ada di direktori

# Counter
count = {"Organik": 0, "Anorganik": 0}
lock = threading.Lock()
prev_centroids = []

# Buka kamera
cap = cv2.VideoCapture(0)


def is_new_object(centroid, prev_centroids, threshold=50):
    for prev in prev_centroids:
        dist = np.linalg.norm(np.array(centroid) - np.array(prev))
        if dist < threshold:
            return False
    return True


def gen_frames():
    global count, prev_centroids
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)[0]
        boxes = results.boxes
        temp_count = {"Organik": 0, "Anorganik": 0}
        current_centroids = []

        for box in boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])

            if conf > 0.5:
                xyxy = box.xyxy[0].cpu().numpy().astype(int)
                x1, y1, x2, y2 = xyxy
                centroid = ((x1 + x2) // 2, (y1 + y2) // 2)
                current_centroids.append(centroid)

                if is_new_object(centroid, prev_centroids):
                    if label in temp_count:
                        temp_count[label] += 1

                # Gambar bounding box dan label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f"{label} {conf:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )

        with lock:
            count["Organik"] += temp_count["Organik"]
            count["Anorganik"] += temp_count["Anorganik"]

        prev_centroids = current_centroids

        # Encode ke JPEG
        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    with lock:
        return render_template(
            "index.html", organik=count["Organik"], anorganik=count["Anorganik"]
        )


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/reset/<kategori>")
def reset(kategori):
    global prev_centroids
    with lock:
        if kategori == "organik":
            count["Organik"] = 0
        elif kategori == "anorganik":
            count["Anorganik"] = 0
        prev_centroids = []  # Reset cache objek agar tidak duplikat deteksi
    return redirect(url_for("index"))


@app.route("/get_counts")
def get_counts():
    with lock:
        return jsonify({"organik": count["Organik"], "anorganik": count["Anorganik"]})


if __name__ == "__main__":
    app.run(debug=True)
