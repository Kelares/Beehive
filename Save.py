from button import Button
import json 
import subprocess
import os
class Save(Button):
    def __init__(self, x, y, _width, _height):
        super(Save, self).__init__(x,y,_width,_height,"SAVE")

    def data(self, dictionary):
        with open("data.json", "w+") as f:
            json.dump(dictionary, f)
        print(os.getcwd())
        subprocess.Popen(["venv/bin/python", "image.py"])
