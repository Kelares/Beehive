class Flower(object):
    def __init__(self, x, y, pollen):
        self.x = x
        self.y = y
        self.circle_color = (200,50,0,100)
        self.radius = 35
        self.pollen = pollen
        self.max_pollen = pollen
        self.max_per_bee = 15000
        self.regenerate_rate = 0.1
        self.regen = 0
        self.spawn_rate = 0.01
        
    def render(self):
        self.circle_color = (200,50,0,constrain((self.pollen*255)/10000, 50, 255))
        fill(*self.circle_color)
        circle(self.x, self.y, self.radius)
        fill(255,255,255)
        textAlign(CENTER, CENTER)
        text(str(self.pollen), self.x, self.y)
        
    
    def update(self):
        self.regen += self.regenerate_rate
        if self.regen >= 1:
            self.regen = 0
            self.pollen += 1
            
