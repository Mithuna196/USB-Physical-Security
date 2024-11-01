import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import os
import tempfile
import cv2

class VideoPlayerApp:
    def __init__(self, window, video_source):
        self.window = window
        self.window.title("USB Physical Security For Systems")
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
        image = Image.open("pic1.jpeg")
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(window, image=background_image)
        background_label.place(x=315, y=110)
        background_label.image = background_image

        self.info_Button = tk.Button(window, text='DEVELOPERS INFO', font=('Open Sans', 12, 'bold'), bd=5, bg='DeepSkyBlue4', fg='black',
                                     cursor='hand2', activebackground='black', activeforeground='cyan', width=15, command=self.project_info)
        self.info_Button.place(x=650, y=450)

        self.disable_Button = tk.Button(window, text='DISABLE', font=('Open Sans', 16, 'bold'), bd=5, bg='DeepSkyBlue4', fg='black',
                                        cursor='hand2', activebackground='black', activeforeground='cyan', width=15, command=self.button1_clicked)
        self.disable_Button.place(x=230, y=370)

        self.enableButton = tk.Button(window, text='ENABLE', font=('Open Sans', 16, 'bold'), bd=5, bg='DeepSkyBlue4', fg='black',
                                      cursor='hand2', activebackground='black', activeforeground='cyan', width=15, command=self.button2_clicked)
        self.enableButton.place(x=460, y=370)
        self.exitButton = tk.Button(window, text='EXIT', font=('Open Sans', 12, 'bold'), bd=5, bg='DeepSkyBlue4', fg='black',
                                      cursor='hand2', activebackground='black', activeforeground='cyan', width=12, command=self.button3_clicked)
        self.exitButton.place(x=120, y=450)

        self.project_label = tk.Label(window, text="!!! USB Physical Security !!!", font=("Arial", 20, "bold"), bg="black", fg="white")
        self.project_label.place(x=300, y=20)

        self.project_label1 = tk.Label(window, text="!!!   LOCK YOUR USB PORTS   !!!", font=("Arial", 12, "bold"), bg="black", fg="white")
        self.project_label1.place(x=330, y=310)

        image_button_image = Image.open("register.png")
        button_image = ImageTk.PhotoImage(image_button_image)
        self.image_button = tk.Button(window, image=button_image, command=self.on_button_click, bd=0, bg='black',highlightthickness=0)
        self.image_button.place(x=860, y=10)
        self.image_button.image = button_image  # Keep a reference!

        self.update()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)

    def project_info(self):
        html_code = """
        <!DOCTYPE html>
<html>
<head>
	<title>Project Information</title>
	<meta name="viewport" content="width=device-width,initial-scale=1.0">
	<style>
		body {
		font-family: Arial,sans-serif;
		margin: 0;
		padding: 0;
		background-color: #f2f2f2;
	}
	.container {
		max-width: 800px;
		margin: 0 auto;
		padding: 50px 20px;
		background-color: #fff;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
		border-radius:4px;
		position:relative;
	}



	h1 {
		font-size: 36px;
		margin-bottom: 30px;
	}

	p {
		font-size: 18px;
		line-height: 1.5;
		margin-bottom: 20px;
	}

	table{
		width: 100%;
		margin-bottom: 20px;
		border-collapse:  collapse;
		}

		table td,
		table th {
			padding: 10px;
			text-align: left;
			border: 1px solid #ddd;
		}

		table th {
			background-color: #f2f2f2;
			font-size: 18px;
		}

		@media only screen and (max-width: 600px){
			.container {
				padding: 30px 10px;
			}
			h1 {
				font-size: 24px;
			}
			p {
				font-size: 16px;
			}
			.photo {
				width: 100px;
				height: 100px;
				top: 10px;
				right: 10px;
			}
			table td,
			table th{
				padding: 5px;
				font-size: 16px;
			}
			table th {
				font-size: 16px;
			}
		}
	</style>
</head>
<body>
	<div class="container">
	<div class="photo"></div>
		<h1>Project Information</h1>
		<p>This project was developed by <strong> Anonymous Hacker</strong> as part of a <strong>Cyber Security Internship.</strong>This project is designed to <strong> secure the Organizations in Real World from Cyber Frauds performed by Hackers.</strong></p>
		<table>
			<thead>
				<tr>
					<th>Project Details</th>
					<th>Value</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>Project Name</td>
					<td>USB Physical Security</td>
				</tr>
				<tr>
					<td>Project Description</td>
					<td>Implementing Physical Security Policy on USB Ports in Organization</td>
				</tr>
				<tr>
					<td>Project Start Date</td>
					<td>22-FEB-2024</td>
				</tr>
				<tr>
					<td>Project End Date</td>
					<td>13-MAR-2024</td>
				</tr>
				<tr>
					<td>Project Status</td>
					<td><strong>Completed</strong></td>
				</tr>
			</tbody>
		</table>
		<h2>Developer Details</h2>
		<table>
			<thead>
				<tr>
					<th>Name</th>
					<th>Email</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>K.Supreethi</td>
					<td>21KB1A0574@nbkrist.org</td>
				</tr>
				<tr>
					<td>G.Mithuna</td>
					<td>21KB1A3024@nbkrist.org</td>
				</tr>
				<tr>
					<td>N.Poojithri</td>
					<td>21KB1A05B7@nbkrist.org</td>
				</tr>
				<tr>
					<td>P.Abhinay Kumar</td>
					<td>21KB1A1242@nbkrist.org</td>
				</tr>
				<tr>
					<td>Y.Rishitha Reddy</td>
					<td>21KB1A05j3@nbkrist.org</td>
				</tr>

		</table>

		<h2>Company Details</h2>
		<table>
			<thead>
				<tr>
					<th>Company</th>
					<th>Contact Mail</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>Name</td>
					<td>Supraja Technologies</td>
				</tr>
				<tr>
					<td>Email</td>
					<td>lockyourusbport@gmail.com</td>
		</table>
        """
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_file:
            temp_file.write(html_code)
            temp_file_path = temp_file.name
            webbrowser.open('file://' + os.path.realpath(temp_file_path))

    def button1_clicked(self):
        self.window.destroy()
        import authenticate2

    def button2_clicked(self):
        self.window.destroy()
        import authenticate1
    def button3_clicked(self):
        quit()

    def on_button_click(self):
        self.window.destroy()
        import login

root = tk.Tk()
video_source = 'home.mp4'
app = VideoPlayerApp(root, video_source)
root.mainloop()
