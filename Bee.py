from random import choice, uniform
class Bee(object):
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.circle_color = (10,10,10,10)
        self._width = 20
        self._height = 1g0
        self.middle = {"x": x, "y": y}
        self.angle = uniform(0, 2*PI)
        self.searching = 0
        

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
        self.search()
            
    def search(self):
        self.searching += 1
        print("SEARCH")
        if self.searching < 20:
            self.x += uniform(2,6) * cos(self.angle)
            self.y += uniform(2,6) * sin(self.angle)
        else:
            self.x += uniform(2,6) * cos(self.angle)
            self.y += uniform(2,6) * sin(self.angle)
            self.angle += uniform(-PI/6, PI/6)
