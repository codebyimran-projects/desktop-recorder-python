import cv2
import numpy as np
import pyautogui
from win32api import GetSystemMetrics
import time
import keyboard

video_name = input("Enter the name of the video file (without extension): ") + ".mp4"
key = keyboard.read_key()
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)
dim = (screen_width, screen_height)
f = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_name, f, 20.0, dim)
print("Recording started... Press 's' to stop.")
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if keyboard.is_pressed('s'):
        print("Recording stopped.")
        break
out.release()
cv2.destroyAllWindows()