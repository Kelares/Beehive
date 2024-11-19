from text_stroke import text_with_border

class Counter(object):
    def __init__(self, x, y, caption, align=(CENTER, TOP), value=0):
        self.x = x
        self.y = y
        self.caption = caption
        self.value = value
        self.align = align
        
    def render(self):
        fill(255,255,255,255)
        textSize(25)
        textAlign(*self.align)
        text_with_border(self.caption.format(str(self.value)), (0,0,0), (255,255,255), self.x, self.y)
