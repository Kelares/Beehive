class Button(object):
    def __init__(self, x, y, _width, _height, caption):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.caption = caption
        self.selected = False
        
    def render(self):
        fill(255,255,255,180)
        rect(self.x, self.y, self._width, self._height)
        textSize(20)
        textAlign(CENTER, CENTER);
        fill(0,255,0,255)
        text(self.caption, self.x+self._width/2, self.y+self._height/2)
        
    def overEvent(self):
        return (self.x <= mouseX <= self.x + self._width and self.y <= mouseY <= self.y + self._height)
    
