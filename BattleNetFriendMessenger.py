from pywinauto import Application
import pyautogui
import time
import win32gui
import win32con

name = str(input("Who would you like to message? "))
msg = str(input("What would you like to say? "))
fav = str(input("Is this friend in your favorites? ")).lower()

# Start up Battle.net, you need to already be signed in
Application().start(r"C:\\Program Files (x86)\\Battle.net\\Battle.net.exe")
time.sleep(3)

# Find our Window and Maximize it for proper calibration
bnetWindow = win32gui.GetForegroundWindow()
win32gui.ShowWindow(bnetWindow, win32con.SW_MAXIMIZE)
width, height = pyautogui.size()
# print("width: " + str(width))
# print("height: " + str(height))
x = width * .9375
y = height * .1018

# Navigate to the Friend Search bar
pyautogui.moveTo(x, y, duration=1)
pyautogui.click()

# Search for name and type them a message
for letter in name:
    pyautogui.hotkey(letter)
time.sleep(3)

# Check if friend is in favorites
if "y" in fav:
    for i in range(3):
        pyautogui.hotkey("tab")
else:
    for i in range(4):
        pyautogui.hotkey("tab")

pyautogui.hotkey("enter")
time.sleep(5) 
for letter in msg:
    pyautogui.hotkey(letter)
pyautogui.hotkey("enter")
