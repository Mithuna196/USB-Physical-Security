import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import subprocess
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import array
import time


class VideoPlayerApp:
    def __init__(self, window, video_source):
        self.count = 0
        self.chances = 0
        self.window = window
        self.window.title("Video Player")

        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)

        self.canvas = tk.Canvas(window, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        def btn1():
             root.destroy()
             import createuser
        def btn2():
             root.destroy()
             import deleteuser 
        def btn3():
             root.destroy()
             import userlimit
        def on_button_click():
            window.destroy()
            import sprint1
        width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)-40
        window.geometry('{}x{}+{}+{}'.format(int(width), int(height), int(x), int(y)))
        self.submitButton = tk.Button(window, text='CREATE  USER', font=('Open Sans', 16, 'bold'), bd=5, bg='cyan', fg='black',
                                      cursor='hand2', activebackground='black', activeforeground='cyan', width=15, command=btn1)
        self.submitButton.place(x=600, y=175)
        self.submitButton = tk.Button(window, text='DELETE  USER', font=('Open Sans', 16, 'bold'), bd=5, bg='cyan', fg='black',
                                      cursor='hand2', activebackground='black', activeforeground='cyan', width=15, command=btn2)
        self.submitButton.place(x=600, y=250)
        self.submitButton = tk.Button(window, text='USER  LIMIT', font=('Open Sans', 16, 'bold'), bd=5, bg='cyan', fg='black',
                                      cursor='hand2', activebackground='black', activeforeground='cyan', width=15, command=btn3)
        self.submitButton.place(x=600, y=325)
        #image_button_image = Image.open("back3.png")
        #button_image = ImageTk.PhotoImage(image_button_image)
        #self.image_button = tk.Button(window, image=button_image, command=on_button_click, bg='black',bd=0, highlightthickness=0)
        #self.image_button.place(x=20, y=20)
        #self.image_button.image = button_image
        self.backButton = tk.Button(window, text='Back', font=('Open Sans', 16, 'bold'), bd=0, bg='cyan', fg='black',
                                      cursor='hand2', activebackground='black', activeforeground='cyan',  command=on_button_click)
        self.backButton.place(x=20, y=20)
        self.update()

    def play_video(self):
        self.cap = cv2.VideoCapture(self.video_source)

    def stop_video(self):
        self.cap.release()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)


root = tk.Tk()
video_source = 'admin.mp4'
app = VideoPlayerApp(root, video_source)
root.mainloop()
