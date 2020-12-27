###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb = color.rgb
#     rgb_colors.append((rgb.r, rgb.g, rgb.b))

# print(rgb_colors)

from turtle import Turtle, Screen
import random

rgb_colors = [
    # (245, 243, 238),
    # (247, 242, 244),
    # (240, 245, 241),
    (202, 164, 109),
    (238, 240, 245),
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (72, 43, 35),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (55, 46, 50),
    (183, 205, 171),
    (36, 60, 74),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (14, 70, 64),
    (30, 68, 100),
    (107, 127, 153),
    (174, 94, 97),
    (176, 192, 209)
]

screen = Screen()
screen.colormode(255)

t = Turtle()
t.shape("turtle")
t.penup()
t.speed("fastest")

# move to bottom left
t.setheading(180)
t.forward(5 * 50)
t.setheading(270)
t.forward(5 * 50)
t.setheading(0)

# draw dots
for _ in range(10):

    for _ in range(10):
        t.color(random.choice(rgb_colors))
        t.dot(20)
        t.forward(50)

    t.setheading(180)
    t.forward(50 * 10)

    t.setheading(90)
    t.forward(50)
    t.setheading(0)


screen.exitonclick()
