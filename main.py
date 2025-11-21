import tkinter as tk
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(410, 270, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=0, pady=20)

wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=1, pady=20)



window.mainloop()

