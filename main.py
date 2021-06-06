import random
from turtle import Turtle, Screen
from random import randint, choice
import colorgram
import pprint


timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.shape("turtle")


# image = "Soup.gif"
# screen.addshape(image)
# timmy.shape(image)

def rnd_rgb():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rnd_rgb_tup = (red, green, blue)
    return rnd_rgb_tup


# Damien Hirst
timmy.speed(0)
timmy.pensize(10)
timmy.penup()
timmy.hideturtle()

xstart = -455
ystart = 380
# xstart = -355
# ystart = 300
timmy.setpos(xstart, ystart)

dot_size = 13
dot_space = 3

colors = colorgram.extract('damien-hirst-lactulose.png', 255)
# pprint.pprint(colors)
# print(len(colors))

usable_colors = []
for color in colors:
    if color.proportion < 0.07:
        # print(color.proportion)
        usable_colors.append(color.rgb)

# pprint.pprint(usable_colors)
circles = len(usable_colors)

while True:
    usable_color = random.choice(usable_colors)
    # timmy.color((usable_color.r, usable_color.g, usable_color.b))
    timmy.dot(dot_size, (usable_color.r, usable_color.g, usable_color.b))
    # timmy.stamp()
    timmy.fd(dot_size * dot_space)
    if timmy.xcor() > (xstart * -1):
        timmy.sety(timmy.ycor() - (dot_size * dot_space))
        timmy.setx(xstart)
    # print(timmy.pos())
    if timmy.ycor() < (ystart * -1):
        # timmy.hideturtle()
        # break
        timmy.setpos(xstart, ystart)

# # Spirograph
# timmy.speed(0)
# red = 0
# green = 0
# blue = 0
# angle_change = 5
# for _ in range(int(360/angle_change)):
#     timmy.circle(100)
#     timmy.left(angle_change)
#     if red < 230:
#         red += int(72/3)
#     elif green < 230:
#         green += int(72/3)
#     elif blue < 230:
#         blue += int(72/3)
#     timmy.color((red, green, blue))
#     timmy.color(rnd_rgb())

# # Abstract line art
# import math
#
# headings = [0, 0, 45, 90, 90, 135, 180, 180, 225, 270, 270, 315]
# speeds = [0, 10, 0, 6, 0, 3, 0, 1, 0]
# dist = 40
#
# timmy.pensize(10)
#
# while True:
#     timmy.color(rnd_rgb())
#     timmy.setheading(random.choice(headings))
#     timmy.speed(random.choice(speeds))
#     #timmy.speed(0)
#     # print(timmy.pos())
#     if (400 > timmy.xcor() > -400) and (400 > timmy.ycor() > -400):
#         if timmy.heading() == 45 or timmy.heading() == 135 or timmy.heading() == 225 or timmy.heading() == 305:
#             timmy.fd(math.sqrt(dist**2 + dist**2))
#         else:
#             timmy.fd(dist)
#     else:
#         timmy.penup()
#         timmy.speed(0)
#         timmy.setpos(randint(0, 300), randint(0, 300))
#         timmy.pendown()


# Polygons
# timmy.color("DeepPink4")
# timmy.penup()
# timmy.setpos(-50, 390)
# timmy.pendown()

# # x sided polygon
# for x in range(3, 25):
#     timmy.color((randint(0, 255), randint(0, 255), randint(0, 255)))
#     for _ in range(x):
#         timmy.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#         timmy.fd(100)
#         timmy.right(360/x)
#
# # Triangle
# for _ in range(3):
#     timmy.fd(100)
#     timmy.right(120)
#
# # Draw a square
# for _ in range(4):
#     timmy.fd(100)
#     timmy.right(90)
#
# for _ in range(5):
#     timmy.fd(100)
#     timmy.right(72)
#
#
# # Dashed line
# # for _ in range(50):
# #     timmy.pendown()
# #     timmy.fd(5)
# #     timmy.penup()
# #     timmy.fd(5)

screen.exitonclick()
