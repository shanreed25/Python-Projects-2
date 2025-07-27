from tkinter import *


window = Tk()
window.title("Miles to Kilometer")
window.minsize(width=300, height=200)
window.config(padx=10, pady=10)


# INPUT***********************************
miles_input = Entry()
miles_input.grid(column=1, row=0)

def miles_to_km():
    miles = int(miles_input.get())
    km = int(miles * 1.60934)
    km_value["text"] = km

# MILES LABEL******************************
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# KM LABEL*********************************
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# EQUAL TO LABEL****************************
equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

# KM VALUE LABEL******************************
km_value = Label(text=0)
km_value.grid(column=1, row=1)

# CALCULATE BUTTON*****************************
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)






window.mainloop()