import cs1elice
from cs1robots import *

load_world('worlds/harvest1.wld') #worlds파일에 있는 rain1.wle 로드

hubo = Robot(beepers = 1)

def go_line():
    for i in range(5):
        hubo.move()
        hubo.pick_beeper() #비퍼 줍기


def turn_right():
    for i in range(3):
        hubo.turn_left()

hubo.move()
hubo.pick_beeper()
go_line()
hubo.turn_left()
hubo.move()
hubo.turn_left()

go_line()
turn_right()

