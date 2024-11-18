from counter import Counter
from Bee import Bee

class Hive(object):
    def __init__(self, x, y, _width, _height, box_color=color(193, 154, 107, 200)):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.pollen = 0
        self.middle = {"x": x + self._width/2, "y": y + self._height/2}
        self.pollen_counter = Counter(width, 0, caption="Pollen: ", align=(RIGHT, TOP))
        self.spawn_threshold = 10000
        self.box_color = box_color
        
    def render(self):
        fill(self.box_color)
        rect(self.x, self.y, self._width, self._height)
        self.pollen_counter.render()

    
    def update(self):
        self.pollen_counter.value = int(self.pollen)
    
    def spawn_bee(self):
        if self.pollen >= self.spawn_threshold:
            self.pollen -= self.spawn_threshold
            spread = self._width
            return Bee(
                x = width/2 + random(-self._width, self._width),
                y = height/2 + random(-self._height, self._height),
                angle = random(0,2*PI),
                hive = self
            ) 
