import json
import os

def get_dimensions(name = "", size = "", obj = None):
    loc = os.path.dirname(os.path.abspath(__file__))
    f = open(loc+"/dimensions/Hardware-Dimensions/json/"+name+".json")
    p = json.loads(f.read())
    for sizes in p[name]:
        if sizes['size'] == size:
            obj.__dict__.update(sizes)
