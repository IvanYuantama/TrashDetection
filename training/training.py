from ultralytics import YOLO

# Load model YOLOv8 pretrained (small)
model = YOLO("yolov8s.pt")  # Bisa diganti ke yolov8m.pt, yolov8l.pt, dll

# Mulai training
model.train(
    data="C:/Users/swati/Downloads/PROYEKWIRUS/datasets/data.yaml",  # path ke data.yaml
    epochs=10,
    imgsz=640,
    batch=16,
    name="sampah_yolov8",
    project="runs/train",
)
