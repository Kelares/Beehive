from Bee import Bee, Activity
from random import randint, uniform
from Flower import Flower
from slider import Slider
from button import Button
from counter import Counter
from textBox import TextBox
from Hive import Hive
from graph import Graph

go = False
_setup = False

def not_middle(direction):
    temp = direction/2
    while abs(temp - direction/2) < 60:
        temp = random(0,direction-direction/20)
    return temp

def setup():
    global ticks, bees, flowers, setup_button, go_button, number_of_bees, number_of_flowers, pace_slider, hive, graph, n_bees_flowers
    size(1200, 1200)
    smooth()
    frameRate(60)
    stroke(255)
    hive = Hive(width/2-20, height/2-20, 40, 40)
    setup_button = Button(0, 0, width/10,50, "setup")
    go_button = Button(width/10, 0, width/10,50, "go")
    
    pace_slider = Slider(0, go_button.y+go_button._height, width/5, height/20, "pace")
    ticks = Counter(width/2, 0, "Ticks: ")
    number_of_bees = TextBox(0, pace_slider.bar.y+pace_slider.bar._height, width/5, 50, "number of bees: ", value="150")
    number_of_flowers = TextBox(0, number_of_bees.y+number_of_bees._height, width/5, 50, "number of flowers: ", value="20")
    n_bees_flowers = {}
    graph = Graph(width-10, height-10, 600, 300, PI)

                             
def draw():
    global ticks, bees, flowers, _setup, go, setup_button, go_button, pace_slider, hive, graph, n_bees_flowers
    background(0)
    ticks.render()
    hive.render()
    if _setup:
        for bee in bees.values():
            bee.render()
        for flower in flowers.values():
            flower.render()
            
        n_bees_flowers[int(ticks.value)] = {"n_bees" : len(bees.keys()), "n_flowers": len(flowers.keys())}
        n_bees = [(tick, n_bees_flowers[tick]["n_bees"]) for tick in n_bees_flowers]
        graph.render([n_bees])
    
    pace_slider.render()
    pace_slider.update()
    setup_button.render()
    go_button.render()
    number_of_bees.render()
    number_of_flowers.render()


    if go:
        ticks.value += 1
        for bee_id, bee in bees.items():
            if bee.activity == Activity.IDLE: 
                observed = {}
                for sec_bee in bees.values():
                    if bee != sec_bee and sec_bee.observed and uniform(0,1) <= 0.01 + sec_bee.observed/90000:
                        observed[sec_bee.observed] = sec_bee.flower

                obs_keys = observed.keys()
                if len(obs_keys):
                    goal = max(obs_keys)
                    flower = observed[goal]
                    bee.activity = Activity.HARVESTING
                    bee.flower = flower
            new_flower = bee.update()
            if bee.lifetime > bee.life_span:
                del(bees[bee_id])
                number_of_bees.value = str(int(number_of_bees.value) - 1)

            if new_flower:
                flowers[id(new_flower)] = new_flower
                
            if bee.activity == Activity.SEARCH:
                for flower in flowers.values():
                    if bee.flower_collision(flower):
                        break
        for flower_id, flower in flowers.items():
            flower.update()
            if flower.pollen == 0:
                del(flowers[flower_id])
                number_of_flowers.value = str(int(number_of_flowers.value) - 1)
                
        hive.update()
        new_bee = hive.spawn_bee()
        if new_bee:
            number_of_bees.value = str(int(number_of_bees.value) + 1)
            bees[id(new_bee)] = new_bee
            
    delay(100 - pace_slider.value)
    
    
def mouseClicked():
    global setup_button, go_button, _setup, go, number_of_bees, number_of_flowers
    if setup_button.overEvent():
        _setup = True
        setup_trigger()
    
    if go_button.overEvent():
        if go:
            go = False
        else:
            print(True)
            go = True
    
    if number_of_bees.overEvent():
        number_of_bees.selected = True
    else:
        number_of_bees.selected = False
    
    if number_of_flowers.overEvent():
        number_of_flowers.selected = True
    else:
        number_of_flowers.selected = False
        
def keyPressed():
    global number_of_bees, number_of_flowers

    if number_of_bees.selected:
        if key == BACKSPACE:
            if number_of_bees.value[:-1] == "":
                number_of_bees.value = 0
            else:
                number_of_bees.value = number_of_bees.value[:-1]
        elif str(key) in [str(i) for i in range(10)]:
            if number_of_bees.value == 0 or number_of_bees.value[0] == "0":
                number_of_bees.value = str(key)
            else:
                number_of_bees.value = str(number_of_bees.value) + str(key)
        
    if number_of_flowers.selected:
        if key == BACKSPACE:
            if number_of_flowers.value[:-1] == "":
                number_of_flowers.value = 0
            else:
                number_of_flowers.value = number_of_flowers.value[:-1]
        elif str(key) in [str(i) for i in range(10)]:
            if number_of_flowers.value == 0 or number_of_flowers.value[0] == "0":
                number_of_flowers.value = str(key)
            else:
                number_of_flowers.value = str(number_of_flowers.value) + str(key)
                
def setup_trigger():
    global bees, flowers, number_of_bees, hive, ticks, number_of_flowers
    human_width = 20
    human_height = 20
    print(number_of_bees.value)
    print( int(number_of_bees.value))
    print(int(number_of_flowers.value))
    spread = 40 
    bees = [
        Bee(
            x = width/2 + random(-hive._width, hive._width),
            y = height/2 + random(-hive._height, hive._height),
            angle = random(0,2*PI),
            hive = hive
        ) for i in range(int(number_of_bees.value))
    ]
    temp = {}
    for bee in bees:
        temp[id(bee)] = bee
    bees = temp
    
    flowers = [
        Flower(
            x=not_middle(width),
            y=not_middle(height),
            pollen=randint(70000,90000)
        ) for i in range(int(number_of_flowers.value))
    ]
    
    temp = {}
    for flower in flowers:
        temp[id(flower)] = flower
    flowers = temp
    ticks.value = 0
    hive.pollen_counter.value = 0

        
