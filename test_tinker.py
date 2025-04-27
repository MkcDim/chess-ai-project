import tkinter as tk

root = tk.Tk()
root.title("Test Tkinter")
root.geometry("200x100")

label = tk.Label(root, text="Ça marche ! 🎉")
label.pack()

root.mainloop()