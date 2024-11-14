class TextBox(object):
    def __init__(self, x, y, _width, _height, caption):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.caption = caption
        self.value = 0
        
    def render(self):
        fill(255,255,255,180)
        rect(self.x, self.y, self._width, self._height)
        textSize(15)
        textAlign(LEFT, CENTER);
        fill(100,160,255,255)
        text(self.caption, self.x, self.y+self._height/2)
        textSize(40)
        textAlign(RIGHT, CENTER);
        text(self.value, self.x+self._width, self.y+self._height/2)
        rect(self.x+self._width-self._width/5, self.y+self._height - self._height/5, self._width/5, self._height/10)
        
    def overEvent(self):
        return (self.x <= mouseX <= self.x + self._width and self.y <= mouseY <= self.y + self._height)
    
