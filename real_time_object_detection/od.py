
import cv2
from ultralytics import YOLO

def main():
    # Load a lightweight YOLO11 model
    model = YOLO("yolo11n.pt")

    # Open the default webcam (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Real-time YOLO detection started.")
    print("Press 'q' to quit.")

    try:
        while True:
            # Read a frame from the webcam
            success, frame = cap.read()

            if not success:
                print("Error: Could not read webcam frame.")
                break

            # Run YOLO object detection
            results = model.predict(
                source=frame,
                conf=0.4,
                imgsz=640,
                verbose=False
            )

            # Draw bounding boxes and labels
            annotated_frame = results[0].plot()

            # Display the live detection window
            cv2.imshow("YOLO Real-Time Object Detection",
                       annotated_frame)

            # Quit when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
