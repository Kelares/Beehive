from __future__ import division
from text_stroke import text_with_border

class Flower(object):
    regenerate_rate = 0.01
    spawn_rate = 0.1
    alive = True
    max_pollen = 90000
    radius = 35
    
    def __init__(self, x, y, pollen):
        self.x = x
        self.y = y
        self._color = [59, 104, 223, 100] #[173, 225, 251, 100]
        self.collision_threshold = self.radius*2
        self.pollen = pollen
        self.max_per_bee = 10000
        self.regen = 0
        self.number_of_leaves = 8
        
    def render(self):
        pushMatrix()
        translate(self.x, self.y)
        self._color[-1] = constrain((self.pollen*150)/10000, 10, 150)
        fill(*self._color)
        stroke(255)
        ellipseMode(CENTER)
        for i in range(self.number_of_leaves):
            rotate(PI*i*2/self.number_of_leaves)
            ellipse(0, 0, self.radius*2, self.radius/2.0)
                
        r, g, b, a = self._color
        # r = 255
        # g = 255
        # b = 0
        # step_r = (0 - r) / (self.radius/2 - 1)
        # step_g = (255 - g) / (self.radius/2 - 1)
        # step_b = (0 - b) / (self.radius/2 - 1)
        
        # Stroke circle
        fill(10,251,0,a)
        circle(0, 0, self.radius)
        # noStroke()        
        # for i in range(self.radius-1, 1, -2):
        #     r += step_r
        #     g += step_g
        #     b += step_b
        #     fill(r,g,b,a)
        #     circle(0, 0, i)
        rotate(PI)
        fill(0)
        textSize(20)
        textAlign(CENTER, CENTER)
        text_with_border(str(self.pollen), (0,0,0), (255,255,255), 0, 0)
        popMatrix()
    
    # def update(self):
    #     if self.pollen < self.max_pollen:
    #         self.regen += self.regenerate_rate
    #         if self.regen >= 1:
    #             self.regen = 0
    #             self.pollen += 1
                
