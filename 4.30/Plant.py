import cs1elice
from cs1robots import *

load_world('worlds/harvest3.wld') #worlds파일에 있는 rain1.wle 로드

hubo = Robot(beepers = 1)

hubo.move()
hubo.move()
hubo.drop_beeper()