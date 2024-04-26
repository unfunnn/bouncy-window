import random
import time
import win32gui
import win32api
import win32con
from os import system

system("cls")

x = win32api.GetSystemMetrics(0)
y = win32api.GetSystemMetrics(1)

answer = ""
print("This program will make any window you choose bounce.")
while answer != "y":
    print("After you push enter, you will have 5 seconds to select the window you want by making it the window in focus")
    input()
    time.sleep(5)
    window = win32gui.GetForegroundWindow()

    print("Caught window: " + "[" + win32gui.GetWindowText(window) + "]")
    answer = input("Is this correct? Y/N: ").lower()

speed = ""
while not speed.isdigit():
    speed = input("How fast would you like it to bounce (numbers only): ")
speed = int(speed)
input("Push enter to have the window start bouncing. To stop it, close the program.")


#window = win32gui.FindWindow(None, "東方神霊廟　～ Ten Desires v1.00c")
#time.sleep(2)

x_speed = random.choice([-speed, speed])
y_speed = random.choice([-speed, speed])

while True:
    current = win32gui.GetWindowRect(window)

    width = current[2] - current[0]
    height = current[3] - current[1]

    #if keyboard.is_pressed("up"):
    #    current[1]-=5
    #if keyboard.is_pressed("left"):
    #    current[0]-=5
    #if keyboard.is_pressed("right"):
    #    current[0]+=5
    #if keyboard.is_pressed("down"):
    #    current[1]+=5

    if current[2] >= x:
        x_speed*=-1
    elif current[0] <= 0:
        x_speed*=-1
    elif current[3] >= y:
        y_speed*=-1
    elif current[1] <= 0:
        y_speed*=-1

    win32gui.MoveWindow(window, int(current[0]+x_speed), int(current[1]+y_speed), width, height, 1)
    time.sleep(1/40)