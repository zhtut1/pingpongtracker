# import cv2
# import numpy as np
# import serial
# import time

# # Set up serial communication with Arduino
# arduino = serial.Serial('COM3', 9600)  # Change 'COM3' to the correct port
# time.sleep(2)  # Wait for the connection to initialize

# def send_score_update(player):
#     if player == 1:
#         arduino.write(b'P1_SCORE_UP\n')
#     elif player == 2:
#         arduino.write(b'P2_SCORE_UP\n')

# def track_ball(frame):
#     # Convert frame to HSV color space for easier color detection
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # Define the range for orange color in HSV
#     lower_orange = np.array([5, 100, 100])
#     upper_orange = np.array([15, 255, 255])

#     # Create a mask for orange color
#     mask = cv2.inRange(hsv, lower_orange, upper_orange)

#     # Find contours in the mask
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Find the largest contour (if any) and its center
#     if contours:
#         largest_contour = max(contours, key=cv2.contourArea)
#         ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
#         if radius > 10:  # Consider only contours with a significant size
#             # Draw a circle around the ball
#             cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255,255), 2)
#             # You can add your logic here to determine if the ball has crossed a specific line or region
#             # to increment the score for player 1 or player 2, for example:
#             # if x < frame_width / 2:
#             #     send_score_update(1)  # Player 1 scores
#             # else:
#             #     send_score_update(2)  # Player 2 scores

#     # Display the resulting frame
#     cv2.imshow('Ping Pong Ball Tracking', frame)

# def main():
#     cap = cv2.VideoCapture(0)  # Change '0' to the appropriate camera index

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         track_ball(frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == '__main__':
#     main()

import cv2
import numpy as np

def track_ball(frame):
    # Convert frame to HSV color space for easier color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for orange color in HSV
    lower_orange = np.array([5, 100, 100])
    upper_orange = np.array([15, 255, 255])

    # Create a mask for orange color
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour (if any) and its center
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
        if radius > 10:  # Consider only contours with a significant size
            # Draw a circle around the ball
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Ping Pong Ball Tracking', frame)

def main():
    cap = cv2.VideoCapture(0)  # Change '0' to the appropriate camera index

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        track_ball(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
