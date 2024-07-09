import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, master, controller):
        self.controller = controller
        self.video_player = None
        self.top_frame = TopFrame(master, controller)
        self.left_frame = LeftFrame(master, controller)
        self.right_frame = RightFrame(master, controller)
        self.centre_frame = CentreFrame(master, controller)

class TopFrame():
       def __init__(self, master, controller):
        self.controller = controller
        self.top_frame = tk.Frame(master, bg="green")
        self.top_frame.pack(side="top", fill="x")

        self.close_icon = tk.PhotoImage(file="icon/icons8-закрыть-10.png")
        self.close_app = tk.Button(self.top_frame, image=self.close_icon, command=master.quit)
        self.close_app.pack(side="right")

        self.detect_video = tk.Button(self.top_frame, text="Обработанное видео")
        self.detect_video.pack(side="left")

class LeftFrame():
    def __init__ (self, master, controller):
        self.controller = controller
        self.left_frame = tk.Frame(master, bg="yellow")
        self.left_frame.pack(side="left", fill="y")

        self.load_btn = tk.Button(self.left_frame, text="Загрузить видео", command=self.controller.load_video)
        self.load_btn.pack()

class RightFrame():
    def __init__(self, master, controller):
        self.controller = controller
        self.right_frame = tk.Frame(master, bg="black")
        self.right_frame.pack(side="right", fill="y")

        self.tree = ttk.Treeview(self.right_frame, columns=("Column1", "Column2"), show='headings')
        self.tree.heading("Column1", text="Номер")
        self.tree.heading("Column2", text="Время проезда")
        self.tree.pack(fill="both", expand=True)

class CentreFrame():
    def __init__(self, master, controller):
        self.controller = controller

        self.centre_frame = tk.Frame(master)
        self.centre_frame.pack(expand=True, fill="x")

        self.canvas = tk.Canvas(self.centre_frame, width=600, height=400)
        self.canvas.pack(expand=True)

        self.button_frame = tk.Frame(self.centre_frame)
        self.button_frame.pack(fill="x", side="bottom")


    def display_media(self, image_tk):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=image_tk)
        self.image_tk = image_tk




