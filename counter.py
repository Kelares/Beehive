class Counter(object):
    def __init__(self, x, y, caption, value=0):
        self.x = x
        self.y = y
        self.caption = caption
        self.value = value
        
    def render(self):
        fill(255,255,255,255)
        textSize(25)
        textAlign(CENTER, TOP)
        text(self.caption + str(self.value), self.x, self.y)
