import tkinter as tk
import os
import platform
from PIL import Image, ImageTk

current_os = platform.system()

if current_os == "Windows":
    icon_path = r"C:\Users\jeffv\OneDrive\Desktop\comp sci\linux\hackerman\images\lego_head_transparent.ico"
else:
    icon_path = r"/home/yourusername/Desktop/lego_head_transparent.png"

user_input = input("Press Enter to run: ")

def run():
    global root
    root = tk.Tk()
    root.title("HackerMan")
    root.configure(bg="black")

    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    else:
        print(f"Warning: Icon file not found at {icon_path}")

    label = tk.Label(root, text = "HackerMan", fg = "green", bg = "black", font=("Arial", 16))
    label.pack(pady = 20)

    root.protocol("WM_DELETE_WINDOW", close)

    root.mainloop()

def close():
    print("Exiting...")
    root.destroy()

if user_input == "":
    run()
else:
    print("Exiting...")
    
