import threading
from tkinter import *
import tkinter as tk 
import pyautogui 
from threading import Thread
from time import sleep
from tkinter import messagebox


class SpamBotMessageBoxes:
    def spam_started(self):
        messagebox.showinfo(title='Info',message='Spam procces started')
    
    def thread_error(self):
        messagebox.showerror(title='Error',message='Spam procces now is running!Please stop it to use start')

    def spam_stopped(self):
        messagebox.showinfo(title='Info',message='Spam procces stoped')


class SpamBot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿) ̄ Spam bot ༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽")
        self.window.config(background='#5ecc7b', height=400, width=500)
        self.__is_spamming = True
        self.__create_widgets()
        self.__message_boxes = SpamBotMessageBoxes()

    def __create_widgets(self):
        self.__spam_entry = Entry()
        self.__spam_entry.place(relx=0.5, rely=0.5, anchor=CENTER, width=300, height=30)
        start_spam_button = Button(text="START", command=self.__start_spam)
        start_spam_button.place(relx=0.5, rely=0.65, anchor=CENTER)
        stop_spam_button = Button(text="STOP", command=self.__stop_spam)
        stop_spam_button.place(relx=0.5, rely=0.75, anchor=CENTER)

    def __spam(self, text: str):
        self.__is_spamming = True
        sleep(5)
        while self.__is_spamming:
            sleep(0.5)
            pyautogui.write(text)
            pyautogui.press('enter')
            
    def __start_spam(self):
        if threading.active_count() == 2:
            self.__message_boxes.thread_error()
        else:
            self.__message_boxes.spam_started()
            thread = Thread(target = lambda: self.__spam(self.__spam_entry.get()),name="spamming_thread")
            thread.start()

    def __stop_spam(self):
        self.__is_spamming = False
        self.__message_boxes.spam_stopped()



if __name__ == "__main__":
    spam_bot = SpamBot()
    spam_bot.window.mainloop()


