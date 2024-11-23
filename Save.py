from button import Button

class Save(Button):
    def __init__(self, x, y, _width, _height):
        super(Save, self).__init__(x,y,_width,_height,"SAVE")

    def data(self, *args):
        print("ASD")
        print(args)
        
        with open("data.csv", "w+") as f:
            print("OPENED")
            for arg in args:
                print(arg)
                f.write("{}\n".format(arg))
