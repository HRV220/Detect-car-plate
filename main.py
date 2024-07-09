import tkinter as tk
from Controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.geometry('1920x1080')
    app = Controller(root)
    root.mainloop()