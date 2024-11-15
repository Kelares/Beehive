class Bar(object):
    def __init__(self, x, y, _width, _height, slider_width):
        self.x = x
        self.y = y
        self._width = _width - slider_width
        self._height = _height
        self.slider_width = slider_width
    
    def render(self):
        fill(255,10,10,200)
        rect(self.x, self.y, self._width + self.slider_width, self._height)
