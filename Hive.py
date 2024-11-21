from counter import Counter
from Bee import Bee

class Hive(object):
    spawn_threshold = 30000

    def __init__(self, x, y, _width, _height, box_color=(193, 154, 107, 200)):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.pollen = 0
        self.middle = {"x": x + self._width/2, "y": y + self._height/2}
        self.pollen_counter = Counter(width, 0, caption="Pollen in the hive: {}", align=(RIGHT, TOP))
        self.box_color = box_color
        self.radius = _width/2
        
    def render(self):
        fill(*self.box_color)
        rect(self.x, self.y, self._width, self._height)
        self.pollen_counter.render()

    
    def update(self):
        self.pollen_counter.value = int(self.pollen)
    
    def spawn_bee(self):
        if self.pollen >= self.spawn_threshold:
            bees = []
            for i in range(self.pollen//self.spawn_threshold):
                self.pollen -= self.spawn_threshold 
                spread = self._width
                bees.append(Bee(
                    x = width/2 + random(-self._width, self._width),
                    y = height/2 + random(-self._height, self._height),
                    angle = random(0,2*PI),
                    hive = self
                ))
            return bees
