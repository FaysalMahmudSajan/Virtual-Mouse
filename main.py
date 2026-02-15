import cv2
import mediapipe as mp
import pyautogui as gu
cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_with,screen_height=gu.size()
index_y,thum_y=0,0
while True:
    _, frame=cap.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame_height,frame_width,_=frame.shape
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                if id==8:
                 cv2.circle(img=frame,center=(x,y),radius=10,color=(26,255,0))
                 index_x=screen_with/frame_width*x
                 index_y=screen_height/frame_height*y
                 gu.moveTo(index_x,index_y)
                 print(index_x, index_y)
                if id==4:
                 cv2.circle(img=frame,center=(x,y),radius=10,color=(255,255,255))
                 thum_x=screen_with/frame_width*x
                 thum_y=screen_height/frame_height*y

                 if abs(index_y-thum_y)<40:
                     gu.click()
                     gu.sleep(1)
                     print("click")
                 else : print("outside")
                 print(thum_x, thum_y)





    # print(hands)
    cv2.imshow('Virtual Mouse',frame)
    cv2.waitKey(1)
