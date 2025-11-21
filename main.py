import random
import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

# ------------------- Taking data from csv ---------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words_data = pd.read_csv("data/french_words.csv")
    to_learn = french_words_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    print(current_card)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    canvas.itemconfig(card_background, image=card_front_image)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))

    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# ---------------------------- UI Build -------------------------------
window = tk.Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(410, 270, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1, pady=20)

wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0, pady=20)

next_card()

window.mainloop()

