from pyexpat import model
from turtle import position
from xml.dom.minidom import Entity
from ursina import *

app = Ursina()

#x-axis, y-axis, z-axis (rotation)
# cube = Entity(model='cube', rotation=(45,45,0)) 

#size on x-axis, y-axis, z-axis
# cube = Entity(model='cube', scale=(3,2,1)) 

# place the thing on x-axis, y-axis, z-axis
# cube = Entity(model='cube', position=(3,2,1))

"""
	Different entity
	cube
	sphere
	circle
	quad
"""

# cube = Entity(model='cube')
# circle = Entity(model='circle')
# sphere = Entity(model='sphere')
quad = Entity(model='quad')
app.run()