import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple", "light blue", "cyan", "magenta"]

brian = turtle.Turtle()


for color in rainbow:
    brian.color(color)
    brian.penup()
    brian.forward(100)
    brian.right(160)
    for side in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        brian.pendown()
        brian.forward(50)
        brian.right(160)
   
