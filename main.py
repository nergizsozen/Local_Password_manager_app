import json
import os
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    from random import choice, randint, shuffle
    import pyperclip
    import json
    import os

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    password = ''.join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Cannot add to file", message="You "
                                                                   "cannot leave "
                                                                   "website or password "
                                                                   "section empty")
    else:
        try:
            with open("data.json", "r") as my_file:
                try:
                    data = json.load(my_file)
                except UnboundLocalError:
                    file_path = "data.json"
                    print("Deleting the existing file because it is empty.")
                    os.remove(file_path)
                else:
                    data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as my_file:
                json.dump(new_data, my_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as my_file:
                json.dump(data, my_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    try:
        with open("data.json", "r") as file:
            file_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="OOoops", message="File doesn't exist")
    else:
        website_input = website_entry.get()
        try:
            dict = file_data[website_input]
        except KeyError:
            messagebox.showinfo(title="Not found", message= "Website credentials does not exist in the file")
        else:
            if website_input in file_data:

                    messagebox.showinfo(title="Data found", message=f"Website:{website_input}\n"
                                                                f"Email: {dict['email']}\n"                                   
                                                                f"Password: {dict['password']}\n")



















# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(row=0, column=1)

#Labels

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=18)
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(END, "nergiz@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

#Buttons
button_search = Button(text="Search",command=search_password)
button_search.grid(row=1, column=2)

button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=33, command=save_info_to_file)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()