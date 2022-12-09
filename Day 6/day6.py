with open("input_day6.txt","r") as f:
    tab_f = f.read().splitlines()
    l = tab_f[0]
    previous = ['x' for _ in range(14)]
    for i,c in enumerate(l) :
        #print(c)
        previous[i%14] = c
        #print(previous)
        s = set(previous)
        if len(s) == 14 and i > 14:
            print(i+1)
            print(s)
            break
        
