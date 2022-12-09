with open("input_day1.txt","r") as f:
    tab_f = f.read().splitlines()
    best = [0,0,0]
    s = 0
    for l in tab_f :
        if l != "" :
            s += int(l)
        else :
            best.sort()
            if s > best[0] :
                best[0] = s
            s = 0
print()
print(best)
print(sum(best))