from cs1media import *

yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

image = load_picture('panda.jpg')

width, height = image.size()

for y in range(height):
    for x in range(width):
        r, g, b = image.get(x, y)
        average_brightness = (r + g + b) // 3
        if average_brightness >= 255.0 * 2 / 3:
            image.set(x, y, yellow)
        elif average_brightness <= 255.0 / 3:
            image.set(x, y, blue)
        else:
            image.set(x, y, green)

image.show()