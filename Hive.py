from counter import Counter
class Hive(object):
    def __init__(self, x, y, _width, _height):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.pollen = 0
        self.middle = {"x": x + self._width/2, "y": y + self._height/2}
        self.pollen_counter = Counter(width, 0, caption="Pollen: ", align=(RIGHT, TOP))
        
    def render(self):
        fill(200,200,10)
        rect(self.x, self.y, self._width, self._height)
        self.pollen_counter.value = int(self.pollen)
        self.pollen_counter.render()
