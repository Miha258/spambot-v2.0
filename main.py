from tkinter import *
import tkinter as tk 
import function

#Window

window = tk.Tk()
window.title("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿) ̄ Spam bot ༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽")
window.config(background='#5ecc7b', height=400, width=500)
spam_entry = Entry()
spam_entry.place(relx=0.5, rely=0.5, anchor=CENTER, width=300, height=30)
start_spam_button = Button(text="START", command=function.start_spam())
start_spam_button.place(relx=0.5, rely=0.65, anchor=CENTER)
stop_spam_button = Button(text="STOP", command=function.stop_spam())
stop_spam_button.place(relx=0.5, rely=0.75, anchor=CENTER)

if __name__ == "__main__":
    window.mainloop()