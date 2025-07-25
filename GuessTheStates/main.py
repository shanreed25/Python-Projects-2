from turtle import Screen, Turtle
import pandas

my_canvas = Screen()
my_canvas.title("U.S States Game")

image = "blank_states_img.gif"

my_canvas.addshape(image)

my_turtle = Turtle()
my_turtle.shape(image)



# Read CSV
states_data = pandas.read_csv("50_states.csv")

# TODO: Get the states column and convert to list
states_column_list = states_data["state"].tolist()

# TODO: Keep track of the score
user_answer_list = []
# TODO: Use a loop to allow the user to keep guessing
while len(user_answer_list) != len(states_column_list):

    # TODO: Get user answer and convert it to title case
    if len(user_answer_list) > 0:
        user_answer = my_canvas.textinput(title=f"{len(user_answer_list)}/{len(states_column_list)} States Correct", prompt="Enter State Name").title()
    else:
        user_answer = my_canvas.textinput(title="Guess The States", prompt="Enter State Name").title()

    if user_answer == "Exit":
        break
    # TODO: Check if user answer is among the 50 states
    if user_answer in states_column_list:
        # get the entire row of data
        # TODO: Get the row where the user answer is equal to the state
        user_answer_row = states_data[states_data.state == user_answer]

        # TODO: Write the correct guesses onto the map using a Turtle
        write_turtle = Turtle()
        write_turtle.hideturtle()
        write_turtle.penup()
        # tapping into the row of data attributes using the name of the rows x and y
        # user_answer_row.x return something like: 17 134, where 17 is an index and 134 is the value of x
        # user_answer_row.x.item() is used to get the single item, which is the actual value of x(134)
        write_turtle.goto(user_answer_row.x.item(), user_answer_row.y.item())

        write_turtle.write(arg=user_answer)
        #OR******************************************
        # write_turtle.write(user_answer_row.state.item())

        # TODO: Record the correct guesses in a list
        user_answer_list.append(user_answer)



# TODO: Generate a csv that contains the states that have not been guessed
# Could have added this inside the if statement with the break statement, before the break statement
print(user_answer_list)

#Using List Comprehension (Recommended for general cases):
# creates a new list containing only the elements from a that are not present in b
# missed_states = [item for item in states_column_list if item not in user_answer_list]
# OR
# use a for loop and if statement
missed_states = []
for state in states_column_list:
    if state not in user_answer_list:
        missed_states.append(state)

print(states_column_list)

my_frame = pandas.DataFrame(missed_states, columns=['State'])
my_frame.to_csv("states_to_learn.csv")


# this is not needed because there is a break statement in the loop
# my_canvas.mainloop()
