from __future__ import division
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
    global ticks, bees, flowers, setup_button, go_button, inp_number_of_bees, inp_number_of_flowers, pace_slider, hive, graph, n_bees_flowers
    global number_of_bees, number_of_flowers, bee_stats, max_follow_chance
    
    size(1200, 1200)
    smooth()
    frameRate(144)
    stroke(255)
    hive = Hive(width/2-20, height/2-20, 40, 40)
    n_bees_flowers = {}
    max_follow_chance = 0.2
    
    setup_button = Button(0, 0, width/10,50, "setup")
    go_button = Button(width/10, 0, width/10,50, "go")
    pace_slider = Slider(0, go_button.y+go_button._height, width/5, height/20, "pace")
    ticks = Counter(width/2, 0, "Ticks: {}")
    inp_number_of_bees = TextBox(0, pace_slider.bar.y+pace_slider.bar._height, width/5, 50, "number of bees: ", value="150")
    inp_number_of_flowers = TextBox(0, inp_number_of_bees.y+inp_number_of_bees._height, width/5, 50, "number of flowers: ", value="35")
    
    graph = Graph(width-30, height-30, 600, 300, PI)

    stats = 1
    number_of_bees = Counter(width, 0 + height/50 * stats, "Number of bees: {}", align=(RIGHT, TOP))
    stats += 1
    number_of_flowers = Counter(width, 0 + height/50 * stats, "Number of flowers: {}", align=(RIGHT, TOP))
    stats += 1
    
    bee_stats = []
    
    DURATION_WAGGLE_DANCE = Counter(width, 0 + height/50 * stats, "Durration of a waggle dance {} ticks", align=(RIGHT, TOP), value=Bee.DURATION_WAGGLE_DANCE)
    bee_stats.append(DURATION_WAGGLE_DANCE)
    stats += 1
    
    max_lifespan = Counter(width, 0 + height/50 * stats, "Maximum bee lifespan {} ticks", align=(RIGHT, TOP), value=Bee.max_lifespan)
    bee_stats.append(max_lifespan)
    stats += 1
    
    min_lifespan = Counter(width, 0 + height/50 * stats, "Minimum bee lifespan {} ticks", align=(RIGHT, TOP), value=Bee.min_lifespan)
    bee_stats.append(min_lifespan)
    stats += 1
    
    # regenerate_rate = Counter(width, 0 + height/50 * stats, "Flower generates pollen every {} ticks", align=(RIGHT, TOP), value=1/Flower.regenerate_rate)
    # bee_stats.append(regenerate_rate)
    # stats += 1
    
    spawn_rate = Counter(width, 0 + height/50 * stats, "Chance for a plant to spawn {}%", align=(RIGHT, TOP), value=Flower.spawn_rate)
    bee_stats.append(spawn_rate)
    stats += 1
        
    spawn_POLLEN = Counter(width, 0 + height/50 * stats, "Pollen needed for a bee to spawn: {}", align=(RIGHT, TOP), value=Hive.spawn_threshold)
    bee_stats.append(spawn_POLLEN)
    stats += 1
        
    max_POLLEN = Counter(width, 0 + height/50 * stats, "Maximum amount of pollen a flower can store: {}", align=(RIGHT, TOP), value=Flower.max_pollen)
    bee_stats.append(max_POLLEN)
    stats += 1
        
    max_follow_dance = Counter(width, 0 + height/50 * stats, "Max follow chance {}%", align=(RIGHT, TOP), value=max_follow_chance)
    bee_stats.append(max_follow_dance)
    stats += 1
    
def draw():
    global ticks, bees, flowers, _setup, go, setup_button, go_button, pace_slider, hive, graph, n_bees_flowers
    global number_of_bees, number_of_flowers, bee_stats, max_follow_chance
    background(0)

    if _setup:
        # for flower in flowers.values():
        #     flower.render()
        # for bee in bees.values():
        #     bee.render()
        
        # if len(n_bees_flowers) >= Graph.max_data:
        #     print(len(n_bees_flowers))
        #     for i, tick in enumerate(n_bees_flowers):
        #         if i % 2 == 0:
        #             del(n_bees_flowers[tick])
                    # print(n_bees_flowers, "END")
                    
        n_bees_flowers[int(ticks.value)] = {"n_bees" : len(bees.keys()), "n_flowers": len(flowers.keys())}
        n_bees = []
        n_flowers =[]
        for tick, item in sorted(n_bees_flowers.iteritems()):
            n_bees.append((tick, item["n_bees"]))
            n_flowers.append((tick, item["n_flowers"]))
        graph.render([((255,255,0), "number of bees", n_bees), ((10, 251, 0, 255), "number of flowers", n_flowers)])
    

        number_of_bees.value = len(bees)
        number_of_bees.render()
    
        number_of_flowers.value = len(flowers)
        number_of_flowers.render()
        
    ticks.render()
    hive.render()
    pace_slider.render()
    pace_slider.update()
    setup_button.render()
    go_button.render()
    inp_number_of_bees.render()
    inp_number_of_flowers.render()
    for bee_stat in bee_stats:
        bee_stat.render()


    if go:
        ticks.value += 1
        for bee_id, bee in bees.items():
            if bee.activity == Activity.IDLE: 
                observed = {}
                for sec_bee in bees.values():
                    if bee != sec_bee and sec_bee.observed and uniform(0,1) <= max_follow_chance * sec_bee.observed/Flower.max_pollen:
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

            if new_flower:
                flowers[id(new_flower)] = new_flower
                
            if bee.activity == Activity.SEARCH:
                for flower in flowers.values():
                    if bee.flower_collision(flower):
                        break
        for flower_id, flower in flowers.items():
            if flower.pollen == 0:
                flowers[flower_id].alive = False
                del(flowers[flower_id])
                
        hive.update()
        new_bees = hive.spawn_bee()
        if new_bees:
            for new_bee in new_bees:
                bees[id(new_bee)] = new_bee
            
    delay(100 - pace_slider.value)
    
def mouseClicked():
    global setup_button, go_button, _setup, go, inp_number_of_bees, inp_number_of_flowers
    if setup_button.overEvent():
        _setup = True
        setup_trigger()
    
    if go_button.overEvent():
        if go:
            go = False
        else:
            print(True)
            go = True
    
    if inp_number_of_bees.overEvent():
        inp_number_of_bees.selected = True
    else:
        inp_number_of_bees.selected = False
    
    if inp_number_of_flowers.overEvent():
        inp_number_of_flowers.selected = True
    else:
        inp_number_of_flowers.selected = False
        
def keyPressed():
    global inp_number_of_bees, inp_number_of_flowers

    if inp_number_of_bees.selected:
        if key == BACKSPACE:
            print(inp_number_of_bees.value)
            print(inp_number_of_bees.value[:-1])
            if inp_number_of_bees.value[:-1] == "":
                inp_number_of_bees.value = "0"
            else:
                inp_number_of_bees.value = inp_number_of_bees.value[:-1]
        elif str(key) in [str(i) for i in range(10)]:
            if inp_number_of_bees.value == 0 or inp_number_of_bees.value[0] == "0":
                inp_number_of_bees.value = str(key)
            else:
                inp_number_of_bees.value = str(inp_number_of_bees.value) + str(key)
        
    if inp_number_of_flowers.selected:
        if key == BACKSPACE:
            if inp_number_of_flowers.value[:-1] == "":
                inp_number_of_flowers.value = "0"
            else:
                inp_number_of_flowers.value = inp_number_of_flowers.value[:-1]
        elif str(key) in [str(i) for i in range(10)]:
            if inp_number_of_flowers.value == 0 or inp_number_of_flowers.value[0] == "0":
                inp_number_of_flowers.value = str(key)
            else:
                inp_number_of_flowers.value = str(inp_number_of_flowers.value) + str(key)
                
def setup_trigger():
    global bees, flowers, inp_number_of_bees, hive, ticks, inp_number_of_flowers, n_bees_flowers
    human_width = 20
    human_height = 20
    print(inp_number_of_bees.value)
    print( int(inp_number_of_bees.value))
    print(int(inp_number_of_flowers.value))
    spread = 40 
    bees = [
        Bee(
            x = width/2 + random(-hive._width, hive._width),
            y = height/2 + random(-hive._height, hive._height),
            angle = random(0,2*PI),
            hive = hive
        ) for i in range(int(inp_number_of_bees.value))
    ]
    temp = {}
    for bee in bees:
        temp[id(bee)] = bee
    bees = temp
    
    coords = [repulsive_coords(hive) for i in range(int(inp_number_of_flowers.value))]
    flowers = [
        Flower(
            x=coord[0],
            y=coord[1],
            pollen=randint(Flower.max_pollen-Flower.max_pollen/5,Flower.max_pollen)
        ) for coord in coords
    ]
    
    temp = {}
    for flower in flowers:
        temp[id(flower)] = flower
    flowers = temp
    ticks.value = 0
    hive.pollen_counter.value = 0
    n_bees_flowers = {}
        
def repulsive_coords(hive):
    x = randint(0+Flower.radius*2, width-Flower.radius*2)
    y = randint(0+Flower.radius*2, height-Flower.radius*2)
    while ((x-hive.x)**2 + (y-hive.y)**2)**(1/2) <= hive.radius*2 + Flower.radius*2:
        x = randint(0+Flower.radius*2, width-Flower.radius*2)
        y = randint(0+Flower.radius*2, height-Flower.radius*2)
    return x,y
                                                                     
                                                                     
                                                                     
