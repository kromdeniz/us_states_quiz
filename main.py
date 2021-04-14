import turtle
import pandas

screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
educ_df = pandas.DataFrame()
turtle = turtle.Turtle()
turtle.hideturtle()
correct_guesses = []
while len(correct_guesses) !=  50:
    guess_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Type a state name: ").title()
    if guess_state in states:
        correct_guesses.append(guess_state)
        cordinates = data[data["state"] == guess_state] # once got the row i can acces the data by .'wanted data'
        # x = int(cordinates["x"])
        # y = int(cordinates["y"])
        turtle.penup()
        turtle.goto(int(cordinates.x),int(cordinates.y))
        turtle.write(guess_state)
        #turtle.write(cordinates.state.item()) returns the first item from the row
    elif guess_state.lower() == "exit":
        for items in states:
            if items not in correct_guesses:
                educ_df = educ_df.append(data[data["state"]==items], ignore_index=True)
                #another way to do it by manipulating lists then converting that list to a dataframe
                #new_list.append(items)
        #new_data = pandas.Framework(new_list) # CONVERTS the list to a data frame
        print(f"The other {len(educ_df)} states are:")
        print(educ_df.state.to_string(index=False))

        break
educ_df["state"].to_csv("The other states.csv", index=0)




