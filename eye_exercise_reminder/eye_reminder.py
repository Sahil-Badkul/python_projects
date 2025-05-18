import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import time
from datetime import datetime
import threading
import random
import os

# Define exercise options with path
ASSET_DIR = "assets"
exercises = [
    {"name": "Blinking", "file": "blinking.gif", "text": "Blink your eyes for 20 seconds 👀"},
    {"name": "Palming", "file": "palming.gif", "text": "Gently palm your eyes to relax 🤲"},
    {"name": "Zooming", "file": "zooming.gif", "text": "Focus on a near and far object 🔍"},
    {"name": "Figure of Eight", "file": "figure_of_eight.gif", "text": "Trace an 8 with your eyes ∞"},
    {"name": "Eye Rolling", "file": "eye_rolling.gif", "text": "Roll your eyes in circular motion 🔄"}
]

def show_gif_notification():
    exercise = random.choice(exercises)
    gif_path = os.path.join(ASSET_DIR, exercise["file"])

    root = tk.Tk()
    root.title(f"👁️ Eye Exercise Reminder – {exercise['name']}")
    root.resizable(False, False)
    root.configure(bg='white')

    # Position bottom-right
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 300
    window_height = 250
    x = screen_width - window_width - 20
    y = screen_height - window_height - 70
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Title
    title = tk.Label(root, text=f"🧘 {exercise['name']} Reminder", font=("Arial", 12, "bold"),
                     bg='white', fg='black')
    title.pack(pady=(10, 5))

    # GIF label
    gif_label = tk.Label(root, bg='white')
    gif_label.pack(pady=5)

    # Message
    message = tk.Label(root, text=exercise['text'], font=("Arial", 11), bg='white', fg='black',
                       wraplength=280, justify='center')
    message.pack(pady=5)

    # Load and resize gif
    try:
        gif = Image.open(gif_path)
    except FileNotFoundError:
        print(f"GIF not found: {gif_path}")
        root.destroy()
        return

    resized_frames = [ImageTk.PhotoImage(
        frame.copy().resize((200, 120), Image.LANCZOS).convert('RGBA'))
        for frame in ImageSequence.Iterator(gif)]

    def animate(index=0):
        gif_label.configure(image=resized_frames[index])
        root.after(100, animate, (index + 1) % len(resized_frames))

    animate()

    # Auto close in 20 seconds
    threading.Timer(20.0, root.destroy).start()
    root.mainloop()

# 🔁 Infinite loop – hourly trigger
while True:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Notification: Exercise reminder.")
    show_gif_notification()
    time.sleep(3600)
