import cs1elice
from cs1robots import *

load_world('worlds/hurdles1.wld') #worlds파일에 있는 rain1.wle 로드

hubo = Robot(beepers = 1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def hurdle():
    hubo.move()
    hubo.turn_left()
    hubo.move()

    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

for i in range(4):
    hurdle()

hubo.move()


