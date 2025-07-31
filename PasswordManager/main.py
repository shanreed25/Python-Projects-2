from tkinter import *
from tkinter import messagebox
import random
import pyperclip



window = Tk()
window.title = "Password Manager"
window.config(padx=50, pady=50)

#--------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # Password Letters**************************************************************
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    # Password Symbols**************************************************************
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    # Password Number***************************************************************
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]
    # print(password_list)

    random.shuffle(password_list)


    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)


    password_textbox.insert(0, password)
    pyperclip.copy(password)

#****************************************************************
# Create a Function to save the password information to a file
def save():
    #TODO: Get the password information
    password_info = []
    website = website_textbox.get()
    username = username_textbox.get()
    password = password_textbox.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("You must complete all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered: \nWebsite: {website}"
                                                              f"\nEmail/Username: {username} \nPassword: {password}"
                                                              f"\nIf your details are correct click OK, otherwise click cancel")
        if is_ok:
            with open("pass.txt", mode='a' ) as file:
                file.write(f"{website} | {username} | {password}\n")
                website_textbox.delete(0, END)
                username_textbox.delete(0, END)
                password_textbox.delete(0, END)
                website_textbox.focus()

# Logo********************************************************************
pass_canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
pass_canvas.create_image(100, 100, image=pass_img)
pass_canvas.grid(row=0, column=1)

# Website Label*******************************************************
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
# Website Textbox
website_textbox = Entry(width=35)
website_textbox.focus()
website_textbox.grid(row=1, column=1, columnspan=2)


# Email/Username Label*******************************************************
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

# Email/Username Textbox
username_textbox = Entry(width=35)

# # Insert a string into the entry box
# username_textbox.insert(0, "myemail@emal.com")
username_textbox.grid(row=2, column=1, columnspan=2)

# Password Label*******************************************************
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Password Textbox
password_textbox = Entry()
password_textbox.grid(row=3, column=1)

# Generate Password*******************************************************
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)


# Add Button*******************************************************
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()



# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #