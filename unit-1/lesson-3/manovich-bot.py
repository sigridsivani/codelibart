import sys
from manovichdata import *
import random

item=random.randrange(3)

theme = sys.argv[1]

if theme == 'numerical':
    print(numerical[item])
elif theme == 'modularity':
    print(modularity[item])
elif theme == 'automation':
    print(automation[item])
elif theme == 'variability':
    print(variability[item])
elif theme == 'transcoding':
    print(transcoding[item])

