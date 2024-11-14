from __future__ import division

from Bar import Bar
class Slider(object):
    def __init__(self, x, y, _width, _height, caption):
        self.x = x
        self.y = y
        self.bar = Bar(x,y, _width, _height)
        self._width = self.bar._width/10
        self._height = self.bar._height
        self.value = 0
        self.new_x = x
        self.caption = caption
        
    def render(self):
        self.value = int((self.x/self.bar._width)*100)
        self.bar.render(self._width)
        fill(100,160,255,180)
        rect(self.x, self.y, self._width, self._height)
        textSize(20)
        textAlign(CENTER, CENTER);
        fill(100,255,255,255)
        text(self.caption + ": " + str(self.value), self.bar.x+self.bar._width/2, self.bar.y + self.bar._height/2)
        
    def overEvent(self):
        return (self.bar.x <= mouseX <= self.bar.x + self.bar._width
                and self.bar.y <= mouseY <= self.bar.y + self.bar._height)
        
        
    def update(self):
        self.over = self.overEvent()
        self.locked = mousePressed and self.over
        if self.locked:
            self.x = mouseX#constrain(mouseX-self._width/2, self.x, self.x + self.bar._width - self._width)
            
        # if abs(self.new_x - self.x) > 1:
        #     self.x = self.new_x
        # if abs(self.newspos - self.spos) > 1:
        #     self.spos = self.spos + (self.newspos - self.spos) / self.loose
