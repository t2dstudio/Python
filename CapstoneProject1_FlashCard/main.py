from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


pd = pandas.read_csv("french_words.csv")
new_dict={key.French:key.English for (index,key) in pd.iterrows()}
random_french, random_english = random.choice(list(new_dict.items()))
def generate_word():
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text=random_french, fill="black")
    canvas.itemconfig(canvas_image, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=back_card_img )
    canvas.itemconfig(card_word, text=random_english,fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")


#............................UI.................................#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
front_card_img = PhotoImage(file="card_front.png")
back_card_img = PhotoImage(file="card_back.png")
canvas_image= canvas.create_image(400,263,image=front_card_img)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

#.....BUTTON.....
wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0,row=1)

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, command=generate_word)
right_button.grid(column=1,row=1)



generate_word()







window.mainloop()

