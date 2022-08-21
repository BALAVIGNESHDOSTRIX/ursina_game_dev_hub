from ursina import *
import random 

def update():
	red = random.randint(0,225)
	green = random.randint(0,225)
	blue = random.randint(0,225)

	cube.color = color.rgb(red, green, blue)


app = Ursina()

cube = Entity(model='cube', color=color.yellow)

app.run()