import cv2
import mediapipe as mp
import pyautogui as gu
import time

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = gu.size()
last_click_time = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_height, frame_width, _ = frame.shape
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            # Index finger tip (ID 8)
            index_landmark = landmarks[8]
            x = int(index_landmark.x * frame_width)
            y = int(index_landmark.y * frame_height)
            cv2.circle(img=frame, center=(x, y), radius=10, color=(26, 255, 0))
            index_x = screen_width / frame_width * x
            index_y = screen_height / frame_height * y
            gu.moveTo(index_x, index_y)

            # Thumb tip (ID 4)
            thumb_landmark = landmarks[4]
            x = int(thumb_landmark.x * frame_width)
            y = int(thumb_landmark.y * frame_height)
            cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 255, 255))
            thumb_y = screen_height / frame_height * y

            if abs(index_y - thumb_y) < 40:
                if time.time() - last_click_time > 1:
                    gu.click()
                    last_click_time = time.time()
                    print("click")

    # print(hands)
    cv2.imshow("Virtual Mouse", frame)
    cv2.waitKey(1)
