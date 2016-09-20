#!/usr/bin/env python3

import tkinter
import os

window = tkinter.Tk()
window.geometry("300x300")
window.configure(bg="blue")
#window.wm_iconbitmap('/home/icon.ico')
window.title("Youtube Downloader")
def doDownload() :
	url = ent.get()
	os.system("youtube-dl "+url)
img = tkinter.PhotoImage(file="logo.gif")
lb = tkinter.Label(window, image=img)
lb.pack()


lbl1 = tkinter.Label(window, text="Download your video now!", fg="White",bg="black")
lbl1.pack()

ent = tkinter.Entry(window)
ent.pack()

btn = tkinter.Button(text="Download Now" , command=doDownload,)
btn.pack()

window.mainloop()

