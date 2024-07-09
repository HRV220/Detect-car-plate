import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from View import View

class Controller:
    def __init__(self, root):
        self.root = root
        self.view = View(self.root, self)
        self.video_playing = False

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.display_image(file_path)

    def load_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            if self.view.video_player:
                self.view.video_player.cap.release()
            self.view.video_player = VideoPlayer(file_path, self.view.centre_frame.canvas)
            self.video_playing = True

    def load_media(self, media_type):
        file_types = [("Image files", "*.jpg;*.jpeg;*.png")] if media_type == "image" else [("Video files", "*.mp4;*.avi;*.mkv")]
        file_path = filedialog.askopenfilename(filetypes=file_types)

        if file_path:
            if media_type == "image":
                self.display_image(file_path)
            elif media_type == "video":
                self.display_video(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        canvas_width = self.view.centre_frame.canvas.winfo_width()
        canvas_height = self.view.centre_frame.canvas.winfo_height()

        # Изменение размера изображения с сохранением пропорций
        image_ratio = image.width / image.height
        canvas_ratio = canvas_width / canvas_height

        if image_ratio > canvas_ratio:
            new_width = canvas_width
            new_height = int(canvas_width / image_ratio)
        else:
            new_height = canvas_height
            new_width = int(canvas_height * image_ratio)

        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)
        self.view.centre_frame.display_media(image_tk)

    def display_video(self, file_path):
        if self.view.video_player:
            self.view.video_player.cap.release()
        self.view.video_player = VideoPlayer(file_path, self.view.centre_frame.canvas)
        self.video_playing = True

    def update_table(self, data):
        for i in self.view.right_frame.tree.get_children():
            self.view.right_frame.tree.delete(i)
        for item in data:
            self.view.right_frame.tree.insert('', 'end', values=item)


class VideoPlayer:
    def __init__(self, video_file, canvas):
        self.cap = cv2.VideoCapture(video_file)
        if not self.cap.isOpened():
            raise ValueError(f"Cannot open video file: {video_file}")
        self.canvas = canvas
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if self.fps == 0:
            raise ValueError(f"Cannot get FPS for video file: {video_file}")
        self.delay = int(1000 / self.fps)
        self.playing = True
        self.update()

    def update(self):
        if self.playing:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
                self.canvas.update()
                self.canvas.after(self.delay, self.update)
            else:
                self.cap.release()







