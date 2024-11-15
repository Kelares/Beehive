from random import choice, uniform

class Bee(object):
    def __init__(self, x, y, angle, hive):
        self.x = x
        self.y = y
        self.angle = angle
        self.circle_color = (10,10,10,10)
        self._width = 20
        self._height = 10
        self.middle = {"x": x, "y": y}
        self.angle = uniform(0, 2*PI)
        self.searching = 0
        self.activity = Activity.IDLE
        self.pollen = 0
        self.flower = None
        self.hive = hive
        
        
    def render(self):
        pushMatrix()
        fill(255,255,0)
        ellipseMode(CENTER)
        translate(self.x, self.y)
        rotate(self.angle)
        ellipse(0, 0, self._width, self._height)
        rotate(-self.angle)
        popMatrix()
        
    def update(self):
        if self.activity == Activity.IDLE and uniform(0,1) <= 0.01:
            self.searching = 1
            self.activity = Activity.SEARCH

        if self.activity == Activity.SEARCH:
            self.search()

        if self.activity == Activity.RETURNING:
            self.returning()
            
        if self.activity == Activity.HARVESTING:
            if abs(int(self.x - self.flower.x)) == 0 and abs(int(self.y - self.flower.y)) == 0:
                self.harvesting(self.flower)
            else:
                self.head_to_flower()

    def search(self):
        self.searching += 1
        if self.searching < 20:
            self.x += uniform(2,6) * cos(self.angle)
            self.y += uniform(2,6) * sin(self.angle)
        elif self.searching >= 200:
            self.activity = Activity.RETURNING
        else:
            self.x += uniform(1,6) * cos(self.angle)
            self.y += uniform(1,6) * sin(self.angle)
            self.angle += uniform(-PI/6, PI/6)
    
    def returning(self):
        # print("RETURNING")
        self.angle = atan2(self.y-self.hive.middle["y"], self.x-self.hive.middle["x"])
        self.x -= uniform(1,6) * cos(self.angle)
        self.y -= uniform(1,6) * sin(self.angle)
        if abs(self.x - self.hive.middle["x"]) <= self.hive._width/2 and abs(self.y - self.hive.middle["y"]) <= self.hive._height/2:
            self.searching = 0
            self.hive.pollen += self.pollen
            self.pollen = 0
            self.activity = Activity.IDLE
            

    def head_to_flower(self):
            self.angle = atan2(self.y-self.flower.y, self.x-self.flower.x)
            self.x -= 1 * cos(self.angle)
            self.y -= 1 * sin(self.angle)
            
    def flower_collision(self, flower):
        if sqrt((self.x - flower.x)**2 + (self.y - flower.y)**2) <= 15:
            print("FOUND")
            self.activity = Activity.HARVESTING
            self.flower = flower
            return True
    
    def harvesting(self, flower):
        print("HARVESTING")
        pollen_amount = 1
        if flower.pollen > 0 and self.pollen <= flower.max_per_bee:
            if self.flower.pollen - pollen_amount <= 0:
                pollen_amount = self.flower.pollen
            
            if pollen_amount == 0.0:
                self.flower = None
                self.activity = Activity.RETURNING
                return None
            
            self.pollen += pollen_amount
            flower.pollen -= pollen_amount
        else:
            self.flower = None
            self.activity = Activity.RETURNING
            
            
            
        
class Activity:
    IDLE = 0
    DANCE = 1
    SEARCH = 2
    RETURNING = 3
    HARVESTING = 4 
