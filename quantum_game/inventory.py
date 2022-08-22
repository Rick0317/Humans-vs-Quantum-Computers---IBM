from ursina import *

class Inventory(Entity):
  def __init__(self, texture="assets/explanation_page.jpg"):
    super().__init__(
      parent = camera.ui,                                         
      model = 'quad',
      scale = (1, 1.2),                                                                              
      position = (0,0),   
      texture=texture,                                                                         
      color = color.white,
    )

class ItemBar(Entity):
  def __init__(self):
    super().__init__(
      parent = camera.ui,
      model = 'quad',
      scale = (0.5, 0.1),
      y = -0.46,
      texture = 'white_cube',                                     
      texture_scale = (5,1),                                      
      color = color.dark_gray 
    )
    self.item_parent = Entity(parent=self, scale=(1,1))
    self.icon1 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (2,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
    self.icon2 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (1,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
    self.icon3 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (0,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
    self.icon4 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (-1,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
    self.icon5 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (-2,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
  

