import cv2

cap = cv2.VideoCapture("highway.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        print(f"Error: Could not read frame {frame_count} or end of video.")
        break

    print(f"Frame {frame_count} dimensions: {frame.shape}")
    frame_count += 1

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if key == 27:  # Escape key
        break

cap.release()
cv2.destroyAllWindows()
