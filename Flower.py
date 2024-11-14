class Flower(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.circle_color = (200,50,0)
        self._width = 20
        self.middle = {"x": x + self._width/2, "y": y + self._width/2}

    def render(self):
        fill(*self.circle_color)
        circle(self.middle["x"], self.middle["y"], self._width)
