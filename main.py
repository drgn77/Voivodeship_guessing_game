import turtle
import pandas
import time

start_time = time.time()
time_limit = 5 * 60


data = pandas.read_csv("data.csv")
all_voivodeship = data.wojewodztwo.to_list()
guessed_voivodeships = []

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Polish voivodeship guessing game")

image = "mapka.gif"
screen.bgpic(image)

while len(guessed_voivodeships) < 16 and (time.time() - start_time < time_limit):


    user_answer = screen.textinput(title=f"{len(guessed_voivodeships)}/16 Guess the voivodeship",
                                   prompt="What's your guess?")
    if user_answer == "exit":
        break
    if user_answer in all_voivodeship:
        guessed_voivodeships.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        voivodeship_data = data[data.wojewodztwo == user_answer].iloc[0]
        t.goto(int(voivodeship_data.x), int(voivodeship_data.y))
        t.write(user_answer)


turtle.mainloop()
