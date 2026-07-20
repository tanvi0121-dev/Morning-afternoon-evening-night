import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My first Tkinter App")
window.geometry("300x200")

#add a label
label = tk.Label(window, text="Hello, Tkinter")
label.pack()

#start the application 
window.mainloop()