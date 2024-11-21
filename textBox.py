from __future__ import division
from text_stroke import text_with_border

class TextBox(object):
    def __init__(self, x, y, _width, _height, caption, value=0, box_color=(187, 207, 141, 150), text_color=(100,255,255,255)):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.caption = caption
        self.value = value
        self.box_color = box_color
        self.text_color = text_color
        self.blink = True
        self.blink_switch = False
        self.last_value = None
        self.caption_size = text_size(self._width/2, self._height, self.caption)

    def render(self):
        pushMatrix()
        translate(self.x, self.y)
        fill(*self.box_color)
        rect(0, 0, self._width, self._height)

            
        textSize(self.caption_size)
        textAlign(LEFT, CENTER);
        text(self.caption, 0,0, self._width/2, self._height)
        text_with_border(self.caption, (0,0,0), self.text_color, 0, self._height/2)
        
        if self.last_value != self.value:
            self.value_size = text_size(self._width/2, self._height, self.value)
            self.last_value = self.value
            
        textSize(self.value_size)
        textAlign(RIGHT, CENTER);
        text(self.value, self._width, self._height/2)
        text_with_border(self.value, (0,0,0), self.text_color,  self._width, self._height/2)
        if self.blink_switch:
            if self.blink:
                self.blink = False
            else:
                rect(self._width-textWidth(self.value)*9/8, self._height/10, self._width/150, self._height - self._height/10)
                self.blink = True
        popMatrix()
        
    def overEvent(self):
        over = (self.x <= mouseX <= self.x + self._width and self.y <= mouseY <= self.y + self._height)
        if over:
            self.blink_switch = True
        else:
            self.blink_switch = False
        return over

def text_with_border(string, stroke_color, fill_color, x, y, thickness=2):
    fill(*stroke_color)
    text(string, x-thickness, y)
    text(string, x+thickness, y)
    text(string, x, y-thickness) 
    text(string, x, y+thickness) 
    fill(*fill_color)
    text(string, x, y) 

def text_size(_width, _height, caption):
    print(textAscent(), textDescent())
    text_width = _width + 1
    text_height = _height + 1
    text_size = 500
    step = 1
    while text_width > _width or text_height > _height:
        textSize(text_size)
        text_width = textWidth(caption)
        text_height = textAscent()+textDescent()
        text_size -= step
    return text_size
