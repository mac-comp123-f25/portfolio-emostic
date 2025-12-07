# Special Pop-up Message for Tyler
# From: Your RA
# Just run this file!

import tkinter as tk
from tkinter import messagebox

# Function for the button
def show_praise():
    messagebox.showinfo(
        "Why You're the Best!",
        "💙 Always there when needed\n"
        "🎯 Makes Kirk Hall a better place\n"
        "✨ Brings positive energy everywhere\n"
        "🤝 Super supportive and caring\n"
        "😄 Has the best sense of humor"
    )

# Create the main window
root = tk.Tk()
root.title("Special Message for Tyler")
root.geometry("350x200")  # window size

# Add a greeting label
label = tk.Label(root, text="HEY TYLER! 👋\nYour RA has a special message for you!", font=("Arial", 15), wraplength=300)
label.pack(pady=10)

# Add the button
button = tk.Button(root, text="Show Message", font=("Arial", 12), command=show_praise)
button.pack(pady=10)

# Run the window
root.mainloop()
