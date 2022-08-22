from ast import In
from logging import root
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import webbrowser
from gates import Gate, Gate_Block
from static_objects import Wall, Axis
from inventory import Inventory, ItemBar
from panda3d.core import AudioSound
from transforms import h_transform, s_transform, x_transform, z_transform, t_transform

app = Ursina()

inventory = Inventory()
Sky()

Entity.default_shader = lit_with_shadows_shader

# General
ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(z=-10, color=color.orange, origin_y=-.5, speed=14)
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
player.cursor.visible=True

# Each axis
x_axis = Axis(position=(5, 5, 10), rotation=(0,0,0))
y_axis = Axis(position=(0, 10, 10), rotation=(0,0,270))
z_axis = Axis(position=(0, 5, 5), rotation=(0,90,0))

zero_vector = Text(text="|0>", parent=scene, position=(-1, 11.5, 10), scale=50)
one_vector = Text(text="|1>", parent=scene, position=(-1, 1, 10), scale=50)
x_letter = Text(text="x-axis", parent=scene, position=(0, 6, 0), scale=50, rotation=(0, 270, 0))
y_letter = Text(text="y-axis", parent=scene, position=(0, 16, 10), scale=50, rotation=(0,0, 90))
z_letter = Text(text="z-axis", parent=scene, position=(6, 6, 10), scale=50)

#Walls
wall_1 = Wall(position=(0,0,32), scale=(64, 10, 1))
wall_2 = Wall(position=(0, 0, -32), scale=(64, 10, 1))
wall_3 = Wall(position=(32, 0, 0), scale=(1, 10, 63))
wall_4 = Wall(position=(-32, 0, 0), scale=(1, 10, 63))

# BlochSphere
bloch_sphere = Entity(model="sphere", collider="box", position = (0, 5, 10), scale=10, color=color.rgba(255,255,255,64))
bs_explanation = Text(text="BlochSphere", position=(-3, 18, 10), scale=100, parent=scene)
quantum_state = Entity(model="arrow", scale=5, color=color.red, rotation_z = 270, position=(0, 7.5, 10))

video1 = 'assets/Qiskit_video_example.mp4'
video_player1 = Entity(model='quad', parent=camera.ui, scale=(1.5, 1), texture=video1, position=(0,0), enabled=False)
video_sound1=loader.loadSfx("assets/Qiskit_sound_example.mp3")

video2 = 'assets/Qiskit_video_example2.mp4'
video_player2 = Entity(model='quad', parent=camera.ui, scale=(1.5, 1), texture=video2, position=(0,0), enabled=False)
video_sound2=loader.loadSfx("assets/Qiskit_video_example2.mp3")

video3 = 'assets/Qiskit_video_example3.mp4'
video_player3 = Entity(model='quad', parent=camera.ui, scale=(1.5, 1), texture=video3, position=(0,0), enabled=False)
video_sound3=loader.loadSfx("assets/Qiskit_video_example3.mp3")

video4 = 'assets/Qiskit_video_example4.mp4'
video_player4 = Entity(model='quad', parent=camera.ui, scale=(1.5, 1), texture=video4, position=(0,0), enabled=False)
video_sound4=loader.loadSfx("assets/Qiskit_video_example4.mp3")

video5 = 'assets/Qiskit_video_example5.mp4'
video_player5 = Entity(model='quad', parent=camera.ui, scale=(1.5, 1), texture=video5, position=(0,0), enabled=False)
video_sound5=loader.loadSfx("assets/Qiskit_video_example5.mp3")

def input(key):
    if key == "1":
        video_player1.enabled = True
        video_player1.texture.synchronizeTo(video_sound1)
        video_sound1.play()
    if key == "2":
        video_player2.enabled = True
        video_player2.texture.synchronizeTo(video_sound2)
        video_sound2.play()
    if key == "3":
        video_player3.enabled = True
        video_player3.texture.synchronizeTo(video_sound3)
        video_sound3.play()
    if key == "4":
        video_player4.enabled = True
        video_player4.texture.synchronizeTo(video_sound4)
        video_sound4.play()
    if key == "5":
        video_player5.enabled = True
        video_player5.texture.synchronizeTo(video_sound5)
        video_sound5.play()
    if key=="n":
        video_player1.enabled=False
        video_sound1.stop()
        video_player2.enabled=False
        video_sound2.stop()
        video_player3.enabled=False
        video_sound3.stop()
        video_player4.enabled=False
        video_sound4.stop()
        video_player5.enabled=False
        video_sound5.stop()
    if key=="m":
        inventory.enabled = False
    if key=="l":
        inventory.enabled = True

# Share the app on twitter
def twitter_share():
    webbrowser.open('https://twitter.com/share?ref_src=twsrc%5Etfw')

# gate transformations

def h_transform2():
    h_transform(quantum_state)

def x_transform2():
    x_transform(quantum_state)

def z_transform2():
    z_transform(quantum_state)
    
def s_transform2():
    s_transform(quantum_state)

def t_transform2():
    t_transform(quantum_state)

def set_back():
    quantum_state.rotation_z = 270
    quantum_state.position=(0, 7.5, 10)


# several gates
h_gate=Gate(position=(0,1,3), icon="assets/h_gate.png")
h_gate2=Gate(position=(0,1,2), icon="assets/h_gate.png", rotation=(0,0,0))
h_gate_block = Gate_Block(position=(0, 0.5, 2.5))

x_gate=Gate(position=(1,1,3), icon="assets/x_gate.png")
x_gate2=Gate(position=(1,1,2), icon="assets/x_gate.png", rotation=(0,0,0))
x_gate_block = Gate_Block(position=(1, 0.5, 2.5))

z_gate=Gate(position=(2,1,3), icon="assets/z_gate.png")
z_gate2=Gate(position=(2,1,2), icon="assets/z_gate.png", rotation=(0,0,0))
z_gate_block = Gate_Block(position=(2, 0.5, 2.5))

s_gate=Gate(position=(3,1,3), icon="assets/s_gate.jpeg")
s_gate2=Gate(position=(3,1,2), icon="assets/s_gate.jpeg", rotation=(0,0,0))
s_gate_block = Gate_Block(position=(3, 0.5, 2.5))

t_gate=Gate(position=(4,1,3), icon="assets/t_gate.png")
t_gate2=Gate(position=(4,1,2), icon="assets/t_gate.png", rotation=(0,0,0))
t_gate_block = Gate_Block(position=(4, 0.5, 2.5))

twitter = Gate(position=(-5, 1, -0.5), icon="assets/twitter.png", rotation=(0,0,0))
twitter_block = Gate_Block(position=(-5, 0.5, 0))

h_gate.on_click = h_transform2
h_gate2.on_click = h_transform2
twitter.on_click = twitter_share

x_gate.on_click = x_transform2
x_gate2.on_click = x_transform2

z_gate.on_click = z_transform2
z_gate2.on_click = z_transform2

s_gate.on_click = s_transform2
s_gate2.on_click = s_transform2

t_gate.on_click = t_transform2
t_gate2.on_click = t_transform2

item_bar = ItemBar()

app.run()