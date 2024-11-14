from Bee import Bee
from random import randint
from Flower import Flower
from slider import Slider
from button import Button
from counter import Counter
from textBox import TextBox

go = False
_setup = False

def not_middle(direction):
    temp = direction/2
    while abs(temp - direction/2) < 60:
        temp = random(0,direction-direction/20)
    return temp

def setup():
    global ticks, bees, flowers, setup_button, go_button, number_of_bees, pace_slider
    size(800, 800)
    setup_button = Button(0, 0, width/10,50, "setup")
    go_button = Button(width/10, 0, width/10,50, "go")
    
    pace_slider = Slider(0, go_button.y+go_button._height, width/5, height/20, "pace")
    ticks = Counter(width/2, 0, "Ticks: ")
    number_of_bees = TextBox(0, pace_slider.bar.y+pace_slider.bar._height, width/5, 50, "number of bees: ")
                             
                             
def draw():
    global ticks, bees, flowers, _setup, go, setup_button, go_button, pace_slider
    background(0,0,0)
    ticks.render()
    if _setup:
        for bee in bees:
            bee.render()
        for flower in flowers:
            flower.render()
    pace_slider.render()
    pace_slider.update()
    setup_button.render()
    go_button.render()
    number_of_bees.render()

    if go:
        ticks.value += 1
        for bee in bees:
            print("ASDDSA")
            bee.update()
    
    delay(100 - pace_slider.value)
    
    
def mouseClicked():
    global setup_button, go_button, _setup, go, number_of_bees
    if setup_button.overEvent():
        _setup = True
        setup_trigger()
    
    if go_button.overEvent():
        if go:
            go = False
        else:
            go = True
    
    if number_of_bees.overEvent():
        number_of_bees.selected = True
    else:
        number_of_bees.selected = False
        
def keyPressed():
    print("PRESSED")
    if number_of_bees.selected:
        if key == BACKSPACE:
            print(key)
            if number_of_bees.value[:-1] == "":
                print(number_of_bees)
                number_of_bees.value = 0
                print(number_of_bees.value)
            else:
                number_of_bees.value = number_of_bees.value[:-1]
        else:
            print(type(key), str(key))
            if number_of_bees.value == 0 or number_of_bees.value[0] == "0":
                number_of_bees.value = str(key)
            else:
                number_of_bees.value = str(number_of_bees.value) + str(key)
        
 
def setup_trigger():
    global bees, flowers, number_of_bees
    human_width = 20
    human_height = 20
    print(number_of_bees.value)
    print( int(number_of_bees.value))
    spread = 40 
    bees = [
        Bee(
            x=width/2 + random(-spread, spread),
            y=height/2 + random(-spread, spread),
            angle = random(0,2*PI)
        ) for i in range(int(number_of_bees.value))
    ]
    
    number_of_flowers = 20
    flowers = [
        Flower(
            x=not_middle(width),
            y=not_middle(height)
        ) for i in range(number_of_flowers)
    ]
