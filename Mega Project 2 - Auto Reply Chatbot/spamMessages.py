import pyautogui
import time
import keyboard
import threading
import pyperclip
import random
import string

def random_string():
    random_string = ""
    length = random.randint(1, 5)
    for i in range(length):
        random_string = random_string + ((random.choice(string.ascii_letters)))
    return random_string

stop_flag = False

def stop():
    global stop_flag
    while True:
        if(keyboard.is_pressed('esc')):
            stop_flag = True
            print("Escape key pressed. Exiting the loop.")
            break
        
listener_thread = threading.Thread(target=stop)
listener_thread.start()

time.sleep(3)

while True:
    if stop_flag:
        break
    
    pyperclip.copy(random_string().capitalize())
    
    pyautogui.click(1200, 970)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
