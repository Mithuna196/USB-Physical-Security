import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

def authenticate():
    if passEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='root', database='login')
            cursor = conn.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity issue,  Please Try Again')
            return

        query = 'select password from temp'

        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            messagebox.showinfo('Error', 'No User Exists')
        elif row[0] == passEntry.get() :
            query = 'DELETE FROM temp'
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','USB PORT ENABLED SUCCESSFULLY')
            enablepass_window.destroy()
            import sprint1
        else:
            query = 'insert into login(email, password) values(%s, %s)'
            cursor.execute(query, (emailEntry.get(), row['password']))
            print(row['password'])
            conn.commit()
            conn.close()
            import authorize1

enablepass_window = tk.Tk()
enablepass_window.title("enable usb port")
enablepass_window.resizable(False, False)

image = Image.open(r"log1.jpg")
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(enablepass_window, image=background_image)
background_label.grid()

heading = tk.Label(enablepass_window, text='ENABLE USB PORT', font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='orchid')
heading.place(x=465, y=100)

passLabel = tk.Label(enablepass_window, text='password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
passLabel.place(x=470, y=200)

passEntry = tk.Entry(enablepass_window, width=30, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
passEntry.place(x=470, y=230)
tk.Frame(enablepass_window, width=250, height=2, bg='orchid1').place(x=470, y=250)

submitButton = tk.Button(enablepass_window, text='ENABLE', font=('Open Sans', 16, 'bold'), bd=0, bg='magenta2', fg='white', cursor='hand2', activebackground='magenta2', activeforeground='white', width=15, command=authenticate)
submitButton.place(x=470, y=390)

enablepass_window.mainloop()
