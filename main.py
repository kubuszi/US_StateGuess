import turtle

screen = turtle.Screen()
screen.title("US State Guess")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
def get_mouse_cor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_cor)

turtle.mainloop()
