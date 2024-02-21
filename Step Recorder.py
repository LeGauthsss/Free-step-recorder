# Author : SELECK Gauthier
# Github : LeGauthsss
# Creation date : 2024 February
# Object : Free step-by-step recorder

# region Libraries
from pynput.mouse import Button, Controller
from pynput import mouse
import pyautogui
import cv2 
import os
import shutil
import tkinter as tk
#py -m pip install numpy
# endregion

# region Variables

# endregion

# region Screenshot
# image = pyautogui.screenshot() 
# image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 
# cv2.imwrite("image1.png", image) 
# src = r"C:\Users\Gauth\image1.png"
# dest = r"C:\Users\Gauth\OneDrive\Bureau\image1.png"
# shutil.move(src, dest)
# endregion

# region Mouse
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    if pressed:
        print('Pressed at {0}'.format((x, y)))
    if not pressed:
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
# endregion

# region Start
def Start():
    buttonStopandReview.config(state=tk.NORMAL)     # enable the button stop and review
    buttonSettings.     config(state=tk.DISABLED)   # disable the button settings
    window.iconify()                                # minimize the window

    global mouse_listener
    while True:
        if mouse_listener is None or not mouse_listener.is_alive():
            mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
            mouse_listener.start()
            
        elif mouse_listener is not None and mouse_listener.is_alive():
            mouse_listener.stop()
            mouse_listener = None
# endregion

# region Stop and Review
def StopandReview():
    buttonStopandReview.config(state=tk.DISABLED)   # disable the button stop and review
    buttonSettings.     config(state=tk.NORMAL)     # enable the button settings
    
    global mouse_listener
    mouse_listener.stop()

    print("Stop and Review")

    # Open the screenshots folder
# endregion

# region Settings
def Settings():
    print("Settings")
# endregion

# region Main Window
window = tk.Tk()
window.title("Step Recorder")
window.geometry("600x200")

global mouse_listener
mouse_listener = None

buttonStart =           tk.Button(window, text="Start",             command=Start)
buttonStopandReview =   tk.Button(window, text="Stop and Review",   command=StopandReview)
buttonSettings =        tk.Button(window, text="Settings",          command=Settings)

buttonStart.pack()
buttonStopandReview.pack()
buttonSettings.pack()

buttonStopandReview.config(state=tk.DISABLED)

window.mainloop()
# endregion