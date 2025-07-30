from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



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

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)

    password_textbox.insert(0, password)
    pyperclip.copy(password)

#****************************************************************
def save():
    #TODO: Get the password information
    password_info = []
    website = website_textbox.get()
    username = username_textbox.get()
    password = password_textbox.get()

    # data to add to json file
    new_data = {
        website : {
                    "username": username,
                    "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("You must complete all fields")
    else:
        # # add json data**************************************************************
       # with open("data.json", mode='w' ) as data_file:
           # json.dump(new_data, data_file, indent=4)# indent is the number of spaces to indent

        # # # read json data**************************************************************
        # with open("data.json", mode='r') as data_file:
        #    # load() takes the json data and converts it to a python dictionary
        #    dict_data = json.load(data_file)
        #    print(dict_data)


        # # update json data**************************************************************
        try:# if this happens, the code goes into the else block
            with open("data.json", mode='r') as data_file:
                #read old data as a dictionary
                dict_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update old data with the new data
            dict_data.update(new_data)# adds data to dictionary
                #save/write upadated data
            with open("data.json", mode='w' ) as data_file:
                json.dump(dict_data, data_file, indent=4)
        finally:
                website_textbox.delete(0, END)
                username_textbox.delete(0, END)
                password_textbox.delete(0, END)
                website_textbox.focus()



# Logo********************************************************************
pass_canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
pass_canvas. create_image(100, 100, image=pass_img)
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