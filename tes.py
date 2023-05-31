# import tkinter as tk
# from tkinter import ttk

# # Fungsi yang akan dijalankan saat tombol diklik
# def button_click():
#     print("Tombol diklik")

# # Membuat instance Tkinter
# root = tk.Tk()

# # Mengatur gaya dan desain kustom
# style = ttk.Style()
# style.configure('TButton', background='green', foreground='red', font=('Arial', 12, 'bold'))

# # Membuat tombol dengan gaya kustom
# button = ttk.Button(root, text="Tombol", style='TButton', command=button_click)
# button.pack(padx=10, pady=5)

# # Menjalankan aplikasi Tkinter
# root.mainloop()

# import tkinter as tk

# # Membuat instance Tkinter
# root = tk.Tk()

# # Mengatur warna latar belakang jendela
# root.configure(background='green')

# # Menjalankan aplikasi Tkinter
# root.mainloop()

# import tkinter as tk

# # Membuat instance Tkinter
# root = tk.Tk()

# # Membuat frame untuk konten
# content_frame = tk.Frame(root)
# content_frame.pack(side="left", fill="both", expand=True)

# # Mengatur warna latar belakang content_frame
# content_frame.configure(background='green')

# # Menjalankan aplikasi Tkinter
# root.mainloop()
# Import the library
from tkinter import *
from tkinter import filedialog

# Create an instance of window
win=Tk()

# Set the geometry of the window
win.geometry("700x350")

# Create a frame widget
frame=Frame(win, width=300, height=300)
frame.grid(row=0, column=0, sticky="NW")

# Create a label widget
label=Label(win, text="I am inside a Frame", font='Arial 17 bold')
label.place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()