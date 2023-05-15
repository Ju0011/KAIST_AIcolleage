import cs1elice
from cs1robots import *

create_world()

#load_world('worlds/rain1.wld') #worlds파일에 있는 rain1.wle 로드
hubo = Robot(beepers = 1)

def Zigzag():

    routin()
    hubo.turn_left()
    hubo.move()

    routin()
    hubo.turn_left()
    hubo.move()

    routin()
    hubo.turn_left()
    hubo.move()

    routin()
    hubo.turn_left()
    hubo.move()

    routin()


def turn_right():
    for i in range(3):
        hubo.turn_left()

def routin():
    hubo.turn_left()
    for i in range(9):
        hubo.move()

    turn_right()
    hubo.move()

    turn_right()
    for i in range(9):
        hubo.move()

Zigzag()