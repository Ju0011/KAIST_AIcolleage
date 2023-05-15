import cs1elice
from cs1robots import *

load_world('worlds/newspaper.wld') #worlds파일에 있는 rain1.wle 로드

hubo = Robot(beepers = 1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

#올라가기
def delivery_1():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

for i in range(4):
    delivery_1()
    hubo.move()

hubo.move()
hubo.turn_left()
hubo.turn_left()

#돌아오기
def delivery_2():
    hubo.move()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

for i in range(4):
    delivery_2()

hubo.move()