import tkinter as tk

points = 0

def on_button_click(command=lambda: on_button_click(button)):
    global points
    points += 1
    button.config(text=str(points))
    print(points)
# Create the main window
root = tk.Tk()
root.title("Button Example")

# Create a button widget
button = tk.Button(root, text="I love you", command=on_button_click)

button.config(command=lambda: on_button_click(button))

button.config(text=points)

# Place the button on the window
button.pack()

# Run the application
root.mainloop()