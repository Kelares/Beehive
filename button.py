from text_stroke import text_with_border

class Button(object):
    def __init__(self, x, y, _width, _height, caption, box_color=(187, 207, 141, 150), text_color=(100,255,255,255)):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.caption = caption
        self.selected = False
        self.box_color = box_color
        self.text_color = text_color
        self.selected_counter = 0
        
    def render(self):
        if self.selected:
            r,g,b,a = self.box_color
            fill(r,255,b,255)
            self.selected_counter += 1
            if self.selected_counter == 3:
                self.selected = False
                self.selected_counter = 0
        else:
            fill(*self.box_color)
        rect(self.x, self.y, self._width, self._height)
        textSize(20)
        textAlign(CENTER, CENTER);
        text_with_border(self.caption, (0,0,0), self.text_color, self.x+self._width/2, self.y+self._height/2)
        
    def overEvent(self):
        self.selected = (self.x <= mouseX <= self.x + self._width and self.y <= mouseY <= self.y + self._height)
        return self.selected
    
