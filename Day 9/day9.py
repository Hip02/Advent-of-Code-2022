import numpy as np

tail_length = 9

visited = set()

H_pos = np.array([0,0])
T_pos = [np.array([0,0]) for i in range(tail_length)]

dir = {'R' : np.array([1,0]), 'L' : np.array([-1,0]), 'U' : np.array([0,1]), 'D' : np.array([0,-1])}

def distance(H_pos, T_pos):
    return H_pos - T_pos

def get_dir(H_pos, T_pos):
    vec = [0,0]
    if (H_pos[0] > T_pos[0]) : vec[0] += 1
    elif (H_pos[0] < T_pos[0]) : vec[0] -= 1
    if (H_pos[1] > T_pos[1]) : vec[1] += 1
    elif (H_pos[1] < T_pos[1]) : vec[1] -= 1
    return np.array(vec)
    

with open("input_day9.txt","r") as f:
    tab_f = f.read().splitlines()
    visited.add((T_pos[tail_length-1][0], T_pos[tail_length-1][1]))
    for line in tab_f:
        mov, count = line.split()
        count = int(count)
        mov = dir[mov]
        for i in range(count):
            H_pos += mov
            #print(f"H goes to {H_pos}")
            d = distance(H_pos, T_pos[0])
            if abs(d[0]) > 1 or abs(d[1]) > 1 :
                T_pos[0] += get_dir(H_pos, T_pos[0])
                #print(f"-> T goes to {T_pos}")
            for j in range(tail_length-1):
                d = distance(T_pos[j], T_pos[j+1])
                if abs(d[0]) > 1 or abs(d[1]) > 1 :
                    T_pos[j+1] += get_dir(T_pos[j], T_pos[j+1])
                    
            visited.add((T_pos[tail_length-1][0], T_pos[tail_length-1][1]))
    
    print(len(visited))

