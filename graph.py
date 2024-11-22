from __future__ import division
from text_stroke import text_with_border

class Graph(object):
    max_data = 1000
    
    def __init__(self, x, y, _width, _height, rotation=0):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.rotation = rotation
        self.max_x = self._width/2
        self.max_y = self._height/2
    
    def render(self, traces):
        pushMatrix()
        fill(50, 50, 50, 50)
        translate(self.x, self.y)
        rotate(self.rotation)
        rect(0, 0, self._width, self._height)
        
        stroke(255)

        # X axis
        arrow_length = self._width/5
        line(0, 0, self._width + arrow_length, 0)
        line(self._width+arrow_length/2, self._height/8, self._width + arrow_length, 0) 
        line(self._width+arrow_length/2, -self._height/8, self._width + arrow_length, 0)
        
        # Y axis
        arrow_length = self._height/3

        line(0, 0, 0, self._height + arrow_length)
        line(0, self._height+arrow_length, self._width/16, self._height+arrow_length/4) 
        line(0, self._height+arrow_length, -self._width/16, self._height+arrow_length/4) 

        strokeWeight(1)

        for _color, label, trace in traces:
            if len(trace) > 1:
                prev = ()
                max_x = max(trace, key=first_ele)[0]
                if self.max_x < max_x:
                    self.max_x = max_x
                
                max_y = max(trace, key=sec_ele)[1] + self._height/20
                if self.max_y < max_y:
                    self.max_y = max_y
                stroke(*_color)         
                prev_x = 0
                for i, data_point in enumerate(trace):
                    prev_x = data_point[0]
                    trace[i] = (self._width * data_point[0] / self.max_x, self._height * (data_point[1] / self.max_y))
                    
                for data_point in trace:
                    if len(prev):
                        line(prev[0], prev[1], data_point[0], data_point[1])
                        prev = data_point
                    else:
                        prev = data_point
        stroke(255)
        strokeWeight(4)

        ticks_x = create_list_with_n_elements(self.max_x, 10)
        ticks_y = create_list_with_n_elements(self.max_y, 10)
        axis_y_ticks = []
        for tick in ticks_y:
            axis_y_ticks.append((tick/self.max_y)*self._height)
            
        max_tick_x = max(ticks_x)
        axis_x_ticks = []
        for tick in ticks_x:
            axis_x_ticks.append((tick/self.max_x)*self._width)
        textSize(20)
        fill(255)
        
        scale(-1, -1)
        textAlign(CENTER, TOP)
        for i, (tick_x) in enumerate(ticks_x):
            text(str(int(tick_x)), -axis_x_ticks[i], 0)
            line(-axis_x_ticks[i], -self._height/30, -axis_x_ticks[i], self._height/30)        
        
        textAlign(LEFT, BOTTOM)
        for i, tick_y in enumerate(ticks_y):
            text(str(int(tick_y)), 0, -axis_y_ticks[i])
            line(-self._width/30, -axis_y_ticks[i], self._width/30, -axis_y_ticks[i])
            
        strokeWeight(16)

        for i, trace in enumerate(traces):
            _color, label, data = trace
            textSize(22)
            textAlign(RIGHT, TOP)
            text_with_border(label, (0,0,0), _color, -self._width/50, -self._height + self._height*(i)/10 + self._height/50, thickness=1)#self._width, self._height - self._height/10)
        textAlign(CENTER, BOTTOM)
        text_with_border("TIME", (0,0,0), (255,255,255), -self._width/2, 0, thickness=2)#self._width, self._height - self._height/10)

        stroke(255)
        strokeWeight(1)

        popMatrix()
 
def create_list_with_n_elements(i, n):
    if n <= 0:
        return [] 
    step = i / (n - 1) if n > 1 else 0  
    return [round(x) for x in [j * step for j in range(n)]]


def first_ele(x):
    return x[0]
       

def sec_ele(x):
    return x[1]
