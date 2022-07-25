import pandas
import turtle



screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

entered_states = []
data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()
input_count = 0
while len(entered_states) < 50:
    input_data = screen.textinput(title=f"You got {len(entered_states)}/{len(list_of_states)}states correctly", prompt="Provide a State Name").title()
    if input_data == "Exit":
        for state in list_of_states:
            if state not in entered_states:
                print(state)
        break

    if input_data in list_of_states:
        state_data = data[data.state == input_data]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(input_data)
        entered_states.append(input_data)
        input_count += 1








#screen.exitonclick()