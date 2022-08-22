from ursina import *

class Wall(Entity):
  def __init__(self, position=(0,0,0), scale=(0,0,0)):
    super().__init__(
      model="cube",
      collider="box", 
      position=position, 
      scale=scale, 
      rotation=(0, 0, 0),
      texture="brick", 
      texture_scale=(5, 5), 
      color=color.rgb(255, 128, 0)
    )

class Axis(Entity):
  def __init__(self, position=(0,0,0), rotation=(0,0,0)):
    super().__init__(
      model="arrow", 
      position=position, 
      scale=10, 
      color=color.rgba(0,0,0,64),
      rotation=rotation
    )

