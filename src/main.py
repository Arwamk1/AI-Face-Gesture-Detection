import cv2
import sys
from detectors import MultiModalDetector
from utils import FPSCounter

def main():
    """
    Main function to run the real-time AI detection application.
    Captures video from the webcam, processes it to detect landmarks,
    and displays the annotated feed with FPS.
    """
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        sys.exit(1)

    # Set camera resolution (optional, can be adjusted)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Initialize detector and FPS counter
    detector = MultiModalDetector()
    fps_counter = FPSCounter()

    print("Starting video stream... Press 'q' to exit.")

    while True:
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Process frame (Face, Hands, Pose)
        output_image = detector.process_and_draw(frame)

        # Calculate and draw FPS
        fps_counter.update()
        fps_counter.draw(output_image)

        # Display the resulting frame
        cv2.imshow('AI Face, Hand & Pose Detection', output_image)

        # Exit on 'q' key press
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
