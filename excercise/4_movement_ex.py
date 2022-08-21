from ursina import *

def update():
	#cube.x = previous x coor + time.dt
	cube.x = cube.x + time.dt
	cube.y = cube.y + time.dt
	cube.z = cube.z - time.dt
	cube.rotation_x = cube.rotation_x + time.dt


app = Ursina()

cube = Entity(model='cube', color=color.red)

app.run()