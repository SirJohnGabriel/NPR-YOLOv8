from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.yaml") 
    model.train(data="config.yaml", epochs=3)
    

if __name__ == "__main__":
    main()