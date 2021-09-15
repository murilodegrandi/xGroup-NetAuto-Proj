import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from PyQt5.QtCore import QProcess

# 1- GUI interface design:

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columns=3,rowspan=3)

# 2- logo design:

logo = Image.open("x1.PNG")
logo = ImageTk.PhotoImage(logo)
logo_lable =tk.Label(image=logo)
logo_lable.image = logo
logo_lable.grid(column=1, row=0)

# 3- notification message for the buttons below:

instructions= tk.Label(root, text="Please Select The Configuration Needed To Be Extracted\n",
                       font="console")
instructions.grid(columnspan=3, column=0, row=1)

# 4- Show Version Configuration and execute it:

show_version = tk.StringVar()
show_version.set("Show Version")
show_version= tk.Button(root, textvariable=show_version, command=lambda:ospf(),
                         font="console", bg="#20bebe", fg="white", height=2, width=15)
show_version.grid(column=1, row=2)

def showversion():

    show_version = "x-filename-and_time.py"
    subprocess.Popen('x-filename-and_time.py', shell=True)
    subprocess.run("python x-filename-and_time.py")
    QProcess.startDetached(show_version)

# 5- SSH Configuration and execute it:

ssh=tk.StringVar()
ssh.set("SSH")
ssh= tk.Button(root, textvariable=ssh, command=lambda:ssh(),
                      font="console", bg="#20bebe", fg="white", height=2, width=15)
ssh.grid(column=1, row=3)

def ssh():

    ssh = "x-filename-and_time.py"
    subprocess.Popen('x-filename-and_time.py', shell=True)
    subprocess.run("python x-filename-and_time.py")
    QProcess.startDetached(ssh)

# 6- OSPF Configuration and execute it:

ospf = tk.StringVar()
ospf.set("OSPF")
ospf= tk.Button(root, textvariable=ospf, command=lambda:ospf(),
                font="console", bg="#20bebe", fg="white", height=2, width=15)
ospf.grid(column=1, row=4)

def ospf():

    ospf_path = "x-filename-and_time.py"
    subprocess.Popen('x-filename-and_time.py', shell=True)
    subprocess.run("python x-filename-and_time.py")
    QProcess.startDetached(ospf_path)


canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columns=3)

root.mainloop()