from __future__ import division
from random import choice, uniform, randint
from Flower import Flower
        
class Activity:
    IDLE = 0
    DANCE = 1
    SEARCH = 2
    RETURNING = 3
    HARVESTING = 4 
    
class Bee(object):
    searching = 0
    activity = Activity.IDLE
    pollen = 0
    flower = None
    observed = None
    SERACH_DURATION = 750
    DURATION_WAGGLE_DANCE = 200
    counter_waggle_dance = 0
    spawn_flower_check = False
    lifetime = 0
    max_lifespan = 1500
    min_lifespan = 1000
    
    def __init__(self, x, y, angle, hive):
        self.x = x
        self.y = y
        self.angle = angle
        self.circle_color = (255,255,0)
        self._width = 10
        self._height = 20
        self.middle = {"x": x, "y": y}
        self.angle = uniform(0, 2*PI)
        self.hive = hive
        self.life_span = randint(self.min_lifespan, self.max_lifespan)

        
    def render(self):
        pushMatrix()
        stroke(0)

        fill(*self.circle_color)
        ellipseMode(CENTER)
        translate(self.x, self.y)
        rotate(self.angle + PI*3/2)
        ellipse(0, 0, self._width, self._height)
        fill(0)
        circle(self._height/10, self._width/2 - self._width/10, min((self._width, self._height))/5)
        circle(-self._height/10, self._width/2 - self._width/10, min((self._width, self._height))/5)
        
        if self.activity == Activity.DANCE:
            temp, self.observed = self.observed, int(self.observed)
            if self.observed != 0:
                stroke(255,0,0)
                # print(self.observed, temp)
                # print("DANCE")
                a = 0
                inc = (PI*6)/self.observed
                prev_x = 0
                prev_y = 0
                for i in range(self.observed):
                    x = i
                    y = self._height/4*sin(a)
                    line(prev_y, prev_x, y, x)
                    prev_x = x
                    prev_y = y
                    a += inc
                noFill();
                stroke(255, 255, 255);
                bezier(0,0, self.observed/2,-40, self.observed/2,self.observed+40, 0, self.observed);
                bezier(0,0, -self.observed/2,-40, -self.observed/2,self.observed+40, 0, self.observed);
            self.observed = temp
        rotate(-self.angle - (PI*3/2))
        stroke(255)
        popMatrix()

            
    def update(self):
        self.lifetime += 1
        if self.activity == Activity.IDLE:
            if self.flower and self.observed:
                self.activity = Activity.DANCE
                
            elif uniform(0,1) <= 0.01:
                # print("SEARCH")
                self.searching = 1
                self.activity = Activity.SEARCH
                
        if self.activity == Activity.DANCE:
            self.counter_waggle_dance += 1
            if self.counter_waggle_dance <= self.DURATION_WAGGLE_DANCE:
                self.angle = atan2(self.flower.y-self.y, self.flower.x-self.x)
            else:
                self.flower = None
                self.observed = None
                self.activity = Activity.IDLE
                self.counter_waggle_dance = 0
            
        if self.activity == Activity.SEARCH:
            self.search()

        if self.activity == Activity.RETURNING:
            self.returning()
            
        if self.activity == Activity.HARVESTING:
            if abs(int(self.x - self.flower.x)) == 0 and abs(int(self.y - self.flower.y)) == 0:
                if self.spawn_flower_check:
                    self.spawn_flower_check = False
                    if self.flower.alive and uniform(0,1) <= self.flower.spawn_rate:
                        return Flower(
                            x = constrain(self.flower.x + random(-width/10, width/10), 0+self.flower.radius*2, width-self.flower.radius*2),
                            y = constrain(self.flower.y + random(-height/10, height/10), 0+self.flower.radius*2, height-self.flower.radius*2),
                            pollen=randint(70000,90000)
                        )
                        
                self.harvesting(self.flower)

            else:
                self.head_to_flower()

    def search(self):
        self.searching += 1
        if self.searching < 20:
            self.x += randint(1,6) * cos(self.angle)
            self.y += randint(1,6) * sin(self.angle)
        elif self.searching >= self.SERACH_DURATION:
            self.activity = Activity.RETURNING
        else:
            self.x += randint(1,6) * cos(self.angle)
            self.y += randint(1,6) * sin(self.angle)
            self.angle += uniform(-PI/6, PI/6)
    
    def returning(self):
        # print("RETURNING")
        self.angle = atan2(self.y-self.hive.middle["y"], self.x-self.hive.middle["x"])
        self.x -= randint(1,6) * cos(self.angle)
        self.y -= randint(1,6) * sin(self.angle)
        if abs(self.x - self.hive.middle["x"]) <= self.hive._width/2 and abs(self.y - self.hive.middle["y"]) <= self.hive._height/2:
            self.searching = 0
            self.hive.pollen += self.pollen
            self.pollen = 0
            self.activity = Activity.IDLE

    def head_to_flower(self):
            self.angle = atan2(self.y-self.flower.y, self.x-self.flower.x)
            self.x -= randint(1,6) * cos(self.angle)
            self.y -= randint(1,6) * sin(self.angle)
            self.spawn_flower_check = True
            
    def flower_collision(self, flower):
        if sqrt((self.x - flower.x)**2 + (self.y - flower.y)**2) <= flower.collision_threshold:
            # print("FOUND")
            self.activity = Activity.HARVESTING
            self.flower = flower
            return True
        
    
    def harvesting(self, flower):
        # print("HARVESTING")
        pollen_amount = 1000
        if flower.pollen > 0 and self.pollen <= flower.max_per_bee:
            if self.flower.pollen - pollen_amount <= 0:
                pollen_amount = self.flower.pollen
            self.pollen += pollen_amount
            flower.pollen -= pollen_amount
        else:
            
            if self.flower.pollen > 0:
                self.observed = self.flower.pollen/1000
            if self.observed:
                self.activity = Activity.RETURNING
            else:
                self.angle = uniform(0, TWO_PI)

                self.activity = Activity.SEARCH

            
            
