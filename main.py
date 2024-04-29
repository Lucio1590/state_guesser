import turtle
import pandas as pd
US_IMAGE = "blank_states_img.gif"
GAME_TITLE = "U.S. States Guesser"

screen = turtle.Screen()
screen.title(GAME_TITLE)
screen.addshape(US_IMAGE)
states = pd.read_csv("50_states.csv")
t = turtle.Turtle()
turtle.penup()
t.penup()
t.speed(0)
screen.tracer(0)
t.hideturtle()
# state, x, y

turtle.shape(US_IMAGE)
game_on = True
states_guessed = 0
screen.update()
prompt = "Name another State"
while game_on:
    guess = screen.textinput(f"Guess the State {states_guessed}/50", prompt)
    if guess == "exit":
        game_on = False
    guess = guess.title()
    temp_state = states.loc[states["state"] == guess]
    if not temp_state.empty:
        guessed_state_x = temp_state["x"].values[0]
        guessed_state_y = temp_state["y"].values[0]
        states_guessed += 1
        t.setpos(guessed_state_x, guessed_state_y)
        t.write(guess, align="center", font=("Arial", 12, "normal"))
        screen.update()
        prompt = "Correct! Guess another State"
        if states_guessed >= 50:
            game_on = False
    else:
        prompt = "Wrong! Try again"
t.setpos(0, 0)
t.write("YOU WON!!", align="center", font=("Arial", 16, "bold"))


turtle.mainloop()
