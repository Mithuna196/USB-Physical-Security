import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Label, Entry, Button, END
import subprocess
import webbrowser
import base64
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import Tk,PhotoImage
import io
import tempfile
import sys
import os
import mysql.connector
import cv2


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
        width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)-40
        window.geometry('{}x{}+{}+{}'.format(int(width), int(height), int(x), int(y)))
        def login_user():
            if self.usernameEntry.get() == '' or self.passwordEntry.get() == '':
                messagebox.showerror('Error', 'All Fields Are Required')
            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='root', database='login')
                    mycursor = conn.cursor()
                except mysql.connector.Error as e:
                    messagebox.showerror('Error', f'Connection Error: {str(e)}')
                    return
                    
                query = 'SELECT * FROM admin WHERE username=%s AND password=%s'
                mycursor.execute(query, (self.usernameEntry.get(), self.passwordEntry.get()))
                row = mycursor.fetchone()
                mycursor.close()
                conn.close()

                if row is None:
                    messagebox.showerror('Error', 'Invalid username or password')
                else:
                    messagebox.showinfo('Welcome', 'Login is successful')
                    self.window.destroy()
                    import admin

        def show():
            self.closeye.config(file='closeye.png')
            self.passwordEntry.config(show ='*')
            self.eyeButton.config(command=hide)

        def hide():
            self.closeye.config(file='openeye.png')    
            self.passwordEntry.config(show='')
            self.eyeButton.config(command=show)

        def user_enter(event):
            if self.usernameEntry.get()=='Username':
                self.usernameEntry.delete(0,END)

        def password_enter(event):
            if self.passwordEntry.get()=='Password':
                self.passwordEntry.delete(0,END)
        def clear():
            self.passwordEntry.delete(0,tk.END)
            self.usernameEntry.delete(0,tk.END)
        def on_button_click():
            window.destroy()
            import sprint1

        self.usernameEntry=tk.Entry(window,width=27,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='black')
        self.usernameEntry.place(x=580,y=225)
        self.usernameEntry.insert(0,'Username')

        self.usernameEntry.bind('<FocusIn>',user_enter)

        self.frame1=tk.Frame(window,width=245,height=2,bg='cyan')
        self.frame1.place(x=580,y=222)
        self.frame1=tk.Frame(window,width=245,height=2,bg='cyan')
        self.frame1.place(x=580,y=248)

        self.passwordEntry=tk.Entry(window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='black')
        self.passwordEntry.place(x=580,y=265)
        self.passwordEntry.insert(0,'Password')
        self.passwordEntry.config(show ='*')

        self.passwordEntry.bind('<FocusIn>',password_enter)

        self.frame2=tk.Frame(window,width=245,height=2,bg='cyan')
        self.frame2.place(x=580,y=262)
        self.frame2=tk.Frame(window,width=245,height=2,bg='cyan')
        self.frame2.place(x=580,y=288)
        self.closeye=PhotoImage(file='closeye.png')
        self.eyeButton=tk.Button(window,image=self.closeye,bd=0,bg='black',activebackground='black',cursor='hand2',command=hide)
        self.eyeButton.place(x=800,y=262)

        self.submitButton = tk.Button(window, text='SUBMIT', font=('Open Sans', 16, 'bold'), bd=3, bg='cyan', fg='black',cursor='hand2', activebackground='black', activeforeground='cyan', width=7, command=login_user)
        self.submitButton.place(x=570,y=325)
        self.clearButton=tk.Button(window,text='CLEAR',font=('Open Sans',16,'bold'),bd=3,bg='cyan',fg='black',activebackground='black',activeforeground='cyan',width=7,command=clear)
        self.clearButton.place(x=720, y=325)       
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
video_source = 'adminlogin.mp4'
app = VideoPlayerApp(root, video_source)
root.mainloop()
