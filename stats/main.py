import tkinter as tk

points = 0

def on_button_click(button):
    global points
    points += 1
    button.config(text=str(points))
# Create the main window
root = tk.Tk()
root.minsize(300, 200)
root.title("Simplicity Clicker")
root.config(bg="black")

# Create a buttons (shop and the clicker button)
button = tk.Button(root, text="I love you", width=10, height=5, command=lambda: on_button_click (button))

button.config()

button.config(text=points)

shop = tk.Button(root, text="shop", width=8, height=4, command=lambda: shop_click(shop))

shop.config()

def shop_click(shop):
    print("shop open sequence")

# Place the button on the window
button.pack(expand=True, anchor="center")
shop.pack()
shop.place(x=5, y=5)

# Run the application
root.mainloop()