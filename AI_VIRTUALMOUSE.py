import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Disable PyAutoGUI fail-safe mechanism
pyautogui.FAILSAFE = False

# Initialize the webcam and hand detection module
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7,
                                          min_tracking_confidence=0.5)
drawing_utils = mp.solutions.drawing_utils

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Initialize variables for finger positions
index_x, index_y = 0, 0
thumb_x, thumb_y = 0, 0

# Smoothing parameters
ALPHA = 0.3  # Smoothing factor

# Colors
cursor_color = (0, 255, 255)
trail_color = (255, 255, 0)

# Trail history
trail_points = []

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands in the frame
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    # Smooth the index finger position
                    index_x = (1 - ALPHA) * index_x + ALPHA * (screen_width / frame_width * x)
                    index_y = (1 - ALPHA) * index_y + ALPHA * (screen_height / frame_height * y)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=cursor_color, thickness=-1)

                if id == 4:
                    # Smooth the thumb finger position
                    thumb_x = (1 - ALPHA) * thumb_x + ALPHA * (screen_width / frame_width * x)
                    thumb_y = (1 - ALPHA) * thumb_y + ALPHA * (screen_height / frame_height * y)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=cursor_color, thickness=-1)

                    # Check the distance between index and thumb fingers
                    distance = np.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)

                    # Move the mouse or click based on finger distance
                    if distance < 25:
                        pyautogui.click(duration=0.1)
                        pyautogui.sleep(0.1)
                    else:
                        # Adjust cursor position to stay within screen boundaries
                        index_x = min(max(index_x, 0), screen_width)
                        index_y = min(max(index_y, 0), screen_height)
                        pyautogui.moveTo(index_x, index_y, duration=0.1)

    # Add visual feedback for cursor movement
    cv2.circle(frame, (int(index_x), int(index_y)), 15, trail_color, -1)
    trail_points.append((int(index_x), int(index_y)))
    for i in range(len(trail_points) - 1):
        cv2.line(frame, trail_points[i], trail_points[i + 1], trail_color, thickness=2)

    # Limit the trail history
    if len(trail_points) > 50:
        trail_points.pop(0)

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
