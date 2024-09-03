import tkinter as tk

points = 0

def on_button_click(command=lambda: on_button_click(button)):
    global points
    points += 1
    button.config(text=str(points))
    print(points)
# Create the main window
root = tk.Tk()
root.title("Simplicity Clicker")

# Create a button widget
button = tk.Button(root, text="I love you", width=5, height=3, command=on_button_click)

button.config(command=lambda: on_button_click(button))

button.config(text=points)

# Place the button on the window
button.pack(expand=True, anchor="center")

# Run the application
root.mainloop()