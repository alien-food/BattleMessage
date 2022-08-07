from pywinauto import Application
import pyautogui
import time
import win32gui
import win32con


class Messenger:
    def __init__(self, pathy: str):
        self.pathy = pathy
        

    def questions(self):
        self.name = str(input("Who would you like to message? "))
        self.msg = str(input("What would you like to say? "))
        self.fav = str(input("Is this friend in your favorites? ")).lower()
        

    def starterup(self):
        Application().start(self.pathy)
        time.sleep(5)
        bnetWindow = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(bnetWindow, win32con.SW_MAXIMIZE)
        width, height = pyautogui.size()
        x = width * .9375
        y = height * .1018
        
        # Navigate to the Friend Search bar
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()


    def BnetMessage(self):
        # Search for name and type them a message
        for letter in self.name:
            pyautogui.hotkey(letter)
        time.sleep(3)

        # Check if friend is in favorites
        if "y" in self.fav:
            for i in range(3):
                pyautogui.hotkey("tab")
        else:
            for i in range(4):
                pyautogui.hotkey("tab")

        pyautogui.hotkey("enter")
        time.sleep(5) 
        for letter in self.msg:
            pyautogui.hotkey(letter)
        pyautogui.hotkey("enter")


Test = Messenger(r"C:\\Program Files (x86)\\Battle.net\\Battle.net.exe")
Test.questions()
Test.starterup()
Test.BnetMessage()
