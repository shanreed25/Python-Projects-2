from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    start_button["state"] = NORMAL
    global reps
    reps = 0
    # stop timer
    window.after_cancel(str(timer))
    # reset Title
    timer_label["text"] = "Timer"
    # reset timer text
    canvas.itemconfig(timer_text, text="00:00")
    # reset checkmarks
    checkmark_label["text"] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    start_button["state"] = DISABLED
    global reps
    reps += 1
    #TODO
    # 1. Work 25 min
    # 2. 5 min Break
    # 3. Work 25 min
    # 4. 5 min Break
    # 5. Work 25 min
    # 6. 5 min Break
    # 7. Work 25 min
    # 8. 20 min Break

    # Equal minutes in seconds**************************************
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text=f"{LONG_BREAK_MIN} MINUTE BREAK", fg=RED)
        count_down(long_break_sec)
        reset()
    elif reps % 2 == 0:
        timer_label.config(text=f" {SHORT_BREAK_MIN} MINUTE BREAK", fg=PINK)
        # print(f"REP: {rep}, short break")
        count_down(short_break_sec)

    else:
        timer_label.config(text=f"Work for {WORK_MIN} minutes")
        count_down(work_sec)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # #TODO: Add checkmark after every session
        # # Every time the countdown completes, it will go into this else statement
        # # reps == to num of sessions
        marks = ""
        # divide the number of reps by 2 to get the number of work sessions
        work_sessions = math.floor(reps / 2) #math.floor() rounds it to the nearest whole number
        print(work_sessions)
        for _ in range(work_sessions):
            marks += "✔️"
            checkmark_label.config(text=marks)


#********************************OR*****************************************************************
# #TODO: Add checkmark after every session
# # # Add or modify text: retrieve the current text using get(), append or modify it, and then update the StringVar using set() again.
# # # Create a StringVar: tkinter.StringVar() will hold the text content for your label
#
#         if reps % 2 == 0: #For every two reps
#                     current_text = checkmark_text.get()
#                     new_text = current_text + "✔️"
#                     checkmark_text.set(new_text)


        # ---------------------------- UI SETUP ------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)





# TIMER LABEL**********************************************************************************************
timer_label = Label(text="Timer",font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# IMAGE**********************************************************************************************
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img )# x = 100 y = 112
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold" ))


canvas.grid(column=1, row=1)


# START BUTTON**********************************************************************************************
start_button = Button(text="Start", bg="white", command=start_timer)
start_button.grid(column=0, row=2)

# CHECKMARK**********************************************************************************************
checkmark_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3,)
# checkmark_text = StringVar()
# checkmark_label.config(textvariable=checkmark_text)
# checkmark_text.set("")

# RESET BUTTON**********************************************************************************************
reset_button = Button(text="Reset", bg="white", command=reset)
reset_button.grid(column=2, row=2)




window.mainloop()