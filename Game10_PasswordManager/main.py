from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_label_input.insert(0, password)
    pyperclip.copy(password) #This is used to copy your string into your clipboard ready to be pasted anywhere
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_label_input.get()
    email = email_label_input.get()
    password = password_label_input.get()

    if len(website)==0 or len(password) == 0:
        messagebox.showinfo(title="Oops ", message="Please make sure you have no empty field")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: "
                                                      f"{password}\n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_label_input.delete(0, END)
                password_label_input.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#window.minsize(width=240,height=240)

canvas =Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

website_label=Label(text="Website:")
website_label.grid(column=0, row=1)

website_label_input=Entry(width=35)
website_label_input.grid(column=1,row=1,columnspan=2)
website_label_input.focus()

email_label=Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_label_input=Entry(width=35)
email_label_input.grid(column=1,row=2,columnspan=2)
email_label_input.insert(0, "t2dstudio@yahoo.com")

password_label=Label(text="Password:")
password_label.grid(column=0, row=3)

password_label_input=Entry(width=21)
password_label_input.grid(column=1, row=3)

password_button=Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button=Button(text="Add", width=35, command=save)
add_button.grid(column=1,row=4, columnspan=2)













window.mainloop()