import tkinter as tk

user_input = input("Press Enter to run: ")

def run():
    global root
    root = tk.Tk()
    root.title("HackerMan")
    root.configure(bg="black")

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
    
