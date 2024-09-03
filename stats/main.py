import tkinter as tk

def on_button_click():
    print("ow!")

# Create the main window
root = tk.Tk(500.500)
root.title("Button Example")

# Create a button widget
button = tk.Button(root, text="try me!!", command=on_button_click)
button.place(x=0,y=0)

# Place the button on the window
button.pack()

# Run the application
root.mainloop()