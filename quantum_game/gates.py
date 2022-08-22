from ursina import *

class Gate(Button):
  def __init__(self, position=(0,0,0), icon="sword",rotation=(90,0,0)):
        super().__init__(
            parent = scene, 
            position = position,
            origin_y= 0.5,
            texture="white-cube",
            color=color.white,
            scale=1,
            highlight_color=color.lime,
            highlight_scale = 1,
            icon=icon,
            rotation=rotation,
        ) 

class Gate_Block(Entity):
  def __init__(self, position=(0,0,0)):
    super().__init__(
      model="cube",
      collider="box", 
      position=position, 
      scale=(1, 1, 1), 
      color=color.white
    )