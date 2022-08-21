from typing import Text
from ursina import *

app = Ursina()


cube = Entity(model='circle', color=color.rgb(255,255,0))

txt = Text(text="I am good", x=-.3, y=-.3, color=color.red)
app.run()