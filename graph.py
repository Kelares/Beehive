from __future__ import division

class Graph(object):
    def __init__(self, x, y, _width, _height, rotation=0):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.rotation = rotation
        self.max_data = 1000
        self.max_x = self._width
        self.max_y = self._height
    
    def render(self, traces):
        pushMatrix()
        fill(100,100,100,100)
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

        stroke(255,0,0)

        prev = ()
        for trace in traces:
            if len(trace) >= self.max_data:
                for i, data_point in enumerate(trace):
                    if i % 2 == 0:
                        del(trace[i])
            
            max_x = max(trace, key=first_ele)[0]
            if self.max_x < max_x:
                self.max_x = max_x
            
            max_y = max(trace, key=sec_ele)[1] + self._height/20
            if self.max_y < max_y:
                self.max_y = max_y
                
                
            if len(trace) > 1:
                for i, data_point in enumerate(trace):
                    trace[i] = (self._width * data_point[0] / self.max_x, self._height * (data_point[1] / self.max_y))
                    
                for data_point in trace:
                    if len(prev):
                        line(prev[0], prev[1], data_point[0], data_point[1])
                        prev = data_point
                    else:
                        prev = data_point
                        
        ticks_x = create_list_with_n_elements(self.max_x, 10)
        ticks_y = create_list_with_n_elements(self.max_y, 10)
        max_tick_y = max(ticks_y)
        axis_y_ticks = []
        for tick in ticks_y:
            axis_y_ticks.append((tick/max_tick_y)*self._height)
            
        textSize(20)
        fill(255)
        scale(-1, -1)
        textAlign(RIGHT, BOTTOM)
        for i, tick_y in enumerate(ticks_y):
            text(str(int(tick_y)), 0, -axis_y_ticks[i])
            line(-self._width/30, -axis_y_ticks[i], self._width/30, -axis_y_ticks[i])
        stroke(255)

        popMatrix()
 
def create_list_with_n_elements(i, n):
    if n <= 0:
        return [] 
    step = i / (n - 1) if n > 1 else 0  
    return [round(x) for x in [j * step for j in range(n)]]


def first_ele(x):
    return x[0]
       

def sec_ele(x):
    return x[0]
