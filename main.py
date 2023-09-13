from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_l = [random.choice(letters) for char in range(nr_letters)]
    password_s = [random.choice(symbols) for char in range(nr_symbols)]
    password_n = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_n + password_s + password_l
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, f"{password}")
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    info_label.config(text="")
    web = website_input.get()
    mail = mail_input.get()
    passw = pass_input.get()
    if web == "" or mail == "" or passw == "":
        messagebox.showerror(title="Info", message="Please don't leave any fields empty!")
        return
    combination = web + " | " + mail + " | " + passw + "\n"

    choise = messagebox.askokcancel(title=web, message=f"These are the details entered: \n"
                                              f"Email: {mail}\nPassword: {passw}\n"
                                              f"Is it OK to save?")
    if choise:
        data_file = open("data.txt", "r")
        if combination not in data_file:
            data_file = open("data.txt", "a")
            data_file.write(combination)

            messagebox.showinfo(title="Info", message="Input added to the file.")
        else:
            messagebox.showwarning(title="Info", message="There is a same input on the file.")
        data_file.close()
        website_input.delete(0, END)
        pass_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")


#LABELS
website_label = Label(text="Website:", bg="white")
website_label.grid(sticky=W, column=0, row=1)
website_label.config(padx=20)


email_label = Label(text="Email/Username:", bg="white")
email_label.grid(sticky=W, column=0, row=2)
email_label.config(padx=20)

pass_label = Label(text="Password:", bg="white")
pass_label.grid(sticky=W, column=0, row=3)
pass_label.config(padx=20)


info_label = Label(text="", bg="white")
info_label.grid(column=1, row=5, columnspan=2)

#INPUTS
website_input = Entry(width=52)
website_input.grid(sticky=W, column=1, row=1, columnspan=2)
website_input.focus()

mail_input = Entry(width=52)
mail_input.grid(sticky=W, column=1, row=2, columnspan=2)
mail_input.insert(0, "example@abc.com")

pass_input = Entry(width=33)
pass_input.grid(sticky=W, column=1, row=3)



#BUTTONS

genpass_button = Button(text="Generate Password", bg="white", command=generate_password)
genpass_button.grid(sticky=W, column=2, row=3)
genpass_button.config(padx=3)

add_button = Button(text="Add", width=44, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)



canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
kilit = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=kilit)
canvas.grid(column=1, row=0)


window.mainloop()