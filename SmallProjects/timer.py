from tkinter import *
import math

window = Tk()
window.title("Timer")
window.config(padx=50, pady=50)

# TIMER LABEL**********************************************************************************************
timer_label = Label(text="Timer")
timer_label.pack()

timer = Label(text="00:00")
timer.pack()

# ---------------------------- START TIMER MECHANISM ------------------------------- #
# Start button triggers this function
def start_timer():
    # function count_down is triggered
    count_down(5 * 60) # 300 seconds or 5 minutes
    #TODO-1
    # count_down(5)# counts down 5 seconds
    # need to change this from seconds to minutes
    # num_of_minutes * 60 = minutes in seconds

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    #TODO-2: Get the minutes
    # we need to divide the seconds by 60, then round down to get the minutes
    # if we have seconds 300
    # but we want it to display in minutes 300 / 60 = 5
    # but if the count has already been going and we had 245 seconds remaining
    # we can get a hold of how many minutes that is equal to
    # minutes: 245 / 60 = 4.0833333, then round down math.floor(245 / 60) = 4 minutes
        # if we round this number down to get rid of all the decimal places
        # it would be equal to 4 minutes
        # we cannot use round() because we only want to round down
        # we can round down by using math.floor() from the math module
    # we can get a hold of how many minutes and seconds that is equal to using
    count_min = math.floor(count / 60)

    #TODO-3: Get the seconds
    # to get the seconds we need to modulo the seconds by 60
    # seconds: 245 % 60
        # since modulo gives us the remainder, the remainder would be the number of seconds left
    count_sec = count % 60
    #TODO-4: When the timer starts make it look like 5:00 instead of 5:0
    # when the timer starts, count_sec has a value of 0
    # so the timer looks like 5:0, but we want 5:00
    # we can use Dynamic Typing
        # Dynamic Typing: changing a variable data type by changing the content the variable holds
    # if count_sec == 0:
    #     count_sec = "00"
    # TODO-5: When the timer get below 10 seconds make it look like 0:09 instead of 0:9
    if count_sec < 10:
        count_sec = f"0{count_sec}"
# Python combines both strong and dynamic typing**************************************************************************************
    # a = "hello"
# Strongly Typed: if holds on to the data type, of a variable
    # it doesn't permit operations between incompatible types without explicit conversion
        # pow(a,3) # will give a TypeError: unsupported operand type for ** or pow(): 'str' and 'int'
# Dynamically Typed: you can dynamically change the type of any variable
    # a = 4

    timer.config(text=f"{count_min}: {count_sec}")
    # will wait 1 second, then call itself
    # passing in 5 - 1, and count become 4
    # the process will continue to repeat going into negative numbers
    # will need to put it inside an if statement to tell it to stop at a certain number
    if count > 0:
        window.after(1000, count_down, count - 1)
        print(count)


# Calls the start_timer function, which calls the count_down function, and the timer starts
start_button = Button(text="Start", bg="white", command=start_timer)
start_button.pack()


window.mainloop()