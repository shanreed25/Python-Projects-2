from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#D4C8FD"
FONT_NAME = "Ariel"

#TODO:Check if there is a words_to_learn.csv file
try: #If it exists, use this data
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:# If the words_to_learn.csv does not exist, then use data in the spanish_words.csv
    data = pandas.read_csv("./data/spanish_words.csv")

#Convert the dataframe to a list
to_learn = data.to_dict(orient="records")


current_card = {}
print(to_learn)



def flip_card():
    # TODO: Show the back of the card
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_lang, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")



def next_card():
    global current_card, flip_timer

    # when the flip_timer is waiting, and you have moved on to a new card
    # the timer does not restart
    # it does not care if you have moved to a new card already
    # whenever we go to a new card, we need a new flip_timer
    # so we need to invalidate the timer, then a new flip timer will start whenever we go to a new card
    window.after_cancel(flip_timer)#cancel the flip timer

    # TODO: Show the front of the card
    current_card = random.choice(to_learn)
    spanish_word = current_card["Spanish"]
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(card_lang, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=spanish_word, fill="black")

    #TODO: Flip card to show the back of card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)#new flip timer that will start whenever we go to a new card

def update_words_to_learn():
    #TODO: Remove current card from to_learn List
    index_to_remove = to_learn.index(current_card)# get index of current card
    removed_card = to_learn.pop(index_to_remove)# Remove card from the to_learn list
    print(removed_card)
    print(to_learn)

    #TODO: Save Updated list to csv file
    df = pandas.DataFrame(to_learn)# Create a DataFrame to_learn list
    df.to_csv("./data/words_to_learn.csv", index=False) # Write dataframe to csv file
    # use index=False if you don't want to create an index for the new csv,
    next_card()



window = Tk()
window.title = "Flashy"
window.config(width=900, height=626, padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_lang = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))

wrong_x = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_x, command=next_card)
unknown_button.config(bg=BACKGROUND_COLOR, relief="flat", borderwidth=0, highlightthickness=0)
unknown_button.grid(row=1,column=0)

right_checkmark = PhotoImage(file="./images/right.png")
known_button = Button(image=right_checkmark, text="known", command=update_words_to_learn)
known_button.config(bg=BACKGROUND_COLOR, relief="flat", borderwidth=0, highlightthickness=0)
known_button.grid(row=1, column=1)


###???????(not sure why I need this flip card timer)
flip_timer = window.after(3000, func=flip_card)

next_card()

window.mainloop()