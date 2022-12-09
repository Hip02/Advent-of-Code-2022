import pprint

map = []

def look_directions(x,y):
    tree = map[y][x]
    found_higher = False
    check_x = x
    while check_x > 0 : 
        check_x -= 1
        if tree <= map[y][check_x] :
            found_higher = True
            break
    if found_higher == False : return False
    found_higher = False
    check_x = x
    while check_x < len(map[0])-1 : 
        check_x += 1
        if tree <= map[y][check_x] :
            found_higher = True
            break
    if found_higher == False : return False
    found_higher = False
    check_y = y
    while check_y > 0 : 
        check_y -= 1
        if tree <= map[check_y][x] :
            found_higher = True
            break
    if found_higher == False : return False
    found_higher = False
    check_y = y
    while check_y < len(map)-1 : 
        check_y += 1
        if tree <= map[check_y][x] :
            found_higher = True
            break
    if found_higher == False : return False

    return True

def get_scenic_score(x,y):
    tree = map[y][x]
    scores = [0,0,0,0]
    check_x = x
    while check_x > 0 : 
        scores[0] += 1
        check_x -= 1
        if tree <= map[y][check_x] :
            break
    check_x = x
    while check_x < len(map[0])-1 : 
        scores[1] += 1
        check_x += 1
        if tree <= map[y][check_x] :
            break
    check_y = y
    while check_y > 0 : 
        scores[2] += 1
        check_y -= 1
        if tree <= map[check_y][x] :
            break
    check_y = y
    while check_y < len(map)-1 : 
        scores[3] += 1
        check_y += 1
        if tree <= map[check_y][x] :
            break
    return scores[0]*scores[1]*scores[2]*scores[3]

counter = 0

with open("input_day8.txt","r") as f:
    tab_f = f.read().splitlines()
    for line in tab_f: map.append([int(line[i]) for i in range(len(line))])
    
    for y,line in enumerate(map) :
        for x,val in enumerate(line) :
            if look_directions(x,y) == False :
                #if x > 0 and x < len(line)-1 and y > 0 and y < len(map)-1 : print(f"y = {y}, x = {x} [{map[y][x]}]")
                counter += 1

    all_scores = []

    for y,line in enumerate(map) :
        for x,val in enumerate(line) :
            score = get_scenic_score(x,y)
            all_scores.append(score)
    

#pprint.pprint(map)

print(counter)

print(max(all_scores))