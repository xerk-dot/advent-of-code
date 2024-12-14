import re
import numpy as np
from aoc import get_input

iters = 0
w, h = 101, 103

def disp(robots):
    area = [['.'  for i in range(w)] for j in range(h)] 
    for l in robots:
        area[l[1]][l[0]] = 'x'
    for l in area:
        print(''.join(l))

nums = np.array([[int(x) for x in re.findall(r'[-]?\d+', y)] for y in     get_input(14).split('\n')])
p, v = nums[:,:2], nums[:,2:]
mods = p.copy()
mods[:,0], mods[:,1] = w, h

while True:
    p = np.remainder(p + v, mods)
    iters += 1
    if np.std(p) <= 20:
        disp(p)
        print(iters)
        break