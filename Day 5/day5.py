cargos = {}
with open("input_day5.txt","r") as f:
    tab_f = f.read().splitlines()
    for l in range(7,-1,-1):
        crates = [tab_f[l][i:i+4] for i in range(0,len(tab_f[l]),4)]
        #crates = list(filter(lambda c: c != '', crates))
        #print(crates)
        for i,c in enumerate(crates) :
            lst = cargos.get(i+1,[])
            if(c[0] == "[") : lst.append(crates[i])
            cargos[i+1] = lst
    

    for l in tab_f[10:]:
        instructions = l.split()
        nb = int(instructions[1])
        f = int(instructions[3])
        to = int(instructions[5])

        items = []
        for i in range(nb):
            item = cargos[f].pop()
            items.append(item)
        
        items = reversed(items)

        lst = cargos.get(to, [])
        for it in items : lst.append(it)

        """for i in range(nb):
            item = cargos[f].pop()
            print(item)
            lst = cargos.get(to, [])
            lst.append(item)"""
    
s = ""
for val in cargos.values():
    s += val[-1][1]

print("PART 1")
print(s)