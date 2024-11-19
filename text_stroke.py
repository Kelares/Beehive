def text_with_border(string, stroke_color, fill_color, x, y, thickness=2):
    fill(*stroke_color)
    text(string, x-thickness, y)
    text(string, x+thickness, y)
    text(string, x, y-thickness) 
    text(string, x, y+thickness) 
    fill(*fill_color)
    text(string, x, y) 
