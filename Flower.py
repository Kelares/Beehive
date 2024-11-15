class Flower(object):
    def __init__(self, x, y, pollen):
        self.x = x
        self.y = y
        self.circle_color = (200,50,0,100)
        self.radius = pollen//2
        self.pollen = pollen
        self.max_pollen = pollen
        self.max_per_bee = 4
        self.regenerate_rate = 0.01
        self.regen = 0
        
    def render(self):
        fill(*self.circle_color)
        circle(self.x, self.y, self.radius)
        fill(255,255,255)
        textAlign(CENTER, CENTER)
        text(str(self.pollen), self.x, self.y)
        self.regen += self.regenerate_rate
        if self.regen >= 1:
            self.regen = 0
            self.pollen += 1
        
