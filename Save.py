from button import Button
import json 
import subprocess
import os
from sys import platform

class Save(Button):
    def __init__(self, x, y, _width, _height):
        super(Save, self).__init__(x,y,_width,_height,"SAVE")

    def data(self, dictionary):
        with open("data.json", "w+") as f:
            json.dump(dictionary, f)
        
        # os.system("cd venv\bin & python ..\..\image.py")
        print("TO SHOW A GRAPH DO THIS IN YOUR CMD LINE", "cd venv\bin & python ..\..\image.py")

        try:
            subprocess.Popen(["venv/bin/python", "image.py"])
        except Exception as e:
            print(e)
            os.chdir("venv\\bin")
            s = subprocess.Popen("python ..\\..\\image.py", shell=True)
            os.chdir("..\\..\\")
