from __future__ import division
from text_stroke import text_with_border

from Bar import Bar
class Slider(object):
    def __init__(self, x, y, _width, _height, caption):
        self.x = x
        self.y = y
        self._width = _width/10
        self._height = _height
        self.value = 0
        self.new_x = x
        self.caption = caption
        self.bar = Bar(x,y, _width, _height, self._width)

    def render(self):
        self.value = constrain(int((self.x/self.bar._width)*100), 0, 100)
        self.bar.render()
        fill(100,160,255,180)
        rect(self.x, self.y, self._width, self._height)
        textSize(20)
        textAlign(CENTER, CENTER);
        fill(100,255,255,255)
        text_with_border(self.caption + ": " + str(self.value), (0,0,0), (100,255,255), self.bar.x+self.bar._width/2, self.bar.y + self.bar._height/2)
        
    def overEvent(self):
        return (self.bar.x <= mouseX <= self.bar.x + self.bar._width + self._width
                and self.bar.y <= mouseY <= self.bar.y + self.bar._height)
        
        
    def update(self):
        self.over = self.overEvent()
        self.locked = mousePressed and self.over
        if self.locked:
            self.x = constrain(mouseX, self.bar.x, self.bar.x+self.bar._width)
