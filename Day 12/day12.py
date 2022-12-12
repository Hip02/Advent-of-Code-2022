import math
import copy

map = []
start = []
L = []

start_char = 'a' #change to 'S' for part 1

with open("input_day12.txt","r") as f:
    tab_f = f.read().splitlines()
    for y,line in enumerate(tab_f):
        l = []
        for x,char in enumerate(line):
            l.append(char)
            if char == start_char :
                start.append((y,x))
        map.append(l)
        
g = ord('a')

g_visited = {}

def visit(pos, visited, count=0) :
    char = map[pos[0]][pos[1]]
    global g
    if ord(char) > g :
        #print(char)
        g += 1
    if char == "S" : char = 'a'
    if char == "E" :
        L.append(count)
        return visited
    count += 1
    my_visited = copy.copy(visited)
    my_visited.add(pos)
    global g_visited
    g_visited[pos] = count
    for y,x in [(-1,0),(1,0),(0,-1),(0,1)]:
            if pos[0] + y >= 0 and pos[0] + y < len(map) and pos[1] + x >= 0 and pos[1] + x < len(map[0]):
                n_char = map[pos[0] + y][pos[1] + x]
                if char == 'z':
                    if n_char == 'E' or n_char == 'z':
                        if (pos[0] + y, pos[1] + x) not in my_visited :
                            v = g_visited.get((pos[0] + y, pos[1] + x), math.inf)
                            if v > count+1:
                                visit((pos[0] + y, pos[1] + x), my_visited, count)
                elif ord(n_char) <= ord(char) + 1 and ord(n_char) >= ord('a'):
                    if (pos[0] + y, pos[1] + x) not in my_visited :
                        v = g_visited.get((pos[0] + y, pos[1] + x), math.inf)
                        if v > count+1:
                            visit((pos[0] + y, pos[1] + x), my_visited, count)
                
for s in start : visit(s,set())

print(sorted(L)[0])
