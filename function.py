import pyautogui 
from threading import Thread
import main
from time import sleep

is_spamming = False

def spam(text: str):
    global is_spamming
    is_spamming = True
    sleep(5)
    while is_spamming:
        sleep(0.1)
        pyautogui.write(text)
        pyautogui.press('enter')
        
def start_spam():
    thread = Thread(target = lambda: spam(main.spam_entry.get()))
    thread.start()

def stop_spam():
    global is_spamming
    is_spamming = False
