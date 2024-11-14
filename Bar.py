class Bar(object):
    def __init__(self, x, y, _width, _height):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height

    
    def render(self, slider_width):
        fill(255,10,10,200)
        rect(self.x, self.y, self._width + slider_width, self._height)
