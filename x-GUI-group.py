import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columns=3,rowspan=3)

logo = Image.open("x1.PNG")
logo = ImageTk.PhotoImage(logo)
logo_lable =tk.Label(image=logo)
logo_lable.image = logo
logo_lable.grid(column=1, row=0)

instructions= tk.Label(root, text="Please Select The Configuration Needed To Be Extracted",
                       font="console")
instructions.grid(columnspan=3, column=0, row=1)

def open_file_version():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a File",
                       filetype=[("pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # print (page_content)

        text_box = tk.Text(root, height=10, width=50,padx=15, pady=15)
        text_box.insert(1.0, page_content)
        # text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=5)
        browse_text.set("Displaying")

def open_file_ssh():
    ssh_text.set("Loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a File",
                       filetype=[("pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # print (page_content)

        text_box = tk.Text(root, height=10, width=50,padx=15, pady=15)
        text_box.insert(1.0, page_content)
        # text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=5)
        ssh_text.set("Displaying")

def open_file_ospf():
    ospf.set("Loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a File",
                       filetype=[("pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # print (page_content)

        ospf_box = tk.Text(root, height=10, width=50,padx=15, pady=15)
        ospf_box.insert(1.0, page_content)
        # text_box.tag_configure("center", justify="center")
        ospf_box.tag_add("center", 1.0, "end")
        ospf_box.grid(column=1, row=5)
        ospf.set("Dispalying")

browse_text=tk.StringVar()
browse_button= tk.Button(root, textvariable=browse_text, command=lambda:open_file_version(),
                         font="console", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Show Version")
browse_button.grid(column=1, row=2)

ssh_text=tk.StringVar()
ssh_button= tk.Button(root, textvariable=ssh_text, command=lambda:open_file_ssh(),
                         font="console", bg="#20bebe", fg="white", height=2, width=15)
ssh_text.set("SSH")
ssh_button.grid(column=1, row=3)

ospf=tk.StringVar()
ospf_button= tk.Button(root, textvariable=ospf, command=lambda:open_file_ospf(),
                         font="console", bg="#20bebe", fg="white", height=2, width=15)
ospf.set("OSPF")
ospf_button.grid(column=1, row=4)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columns=3)

root.mainloop()
