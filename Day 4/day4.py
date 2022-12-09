with open("input_day4.txt","r") as f:
    tab_f = f.read().splitlines()
    cnt = 0
    for l in tab_f:
        p1,p2 = l.split(",")
        p1 = p1.split("-")
        p2 = p2.split("-")
        p1[0] = int(p1[0])
        p1[1] = int(p1[1])
        p2[0] = int(p2[0])
        p2[1] = int(p2[1])
        I1 = set([i for i in range(p1[0],p1[1]+1)])
        I2 = set([i for i in range(p2[0],p2[1]+1)])
        inter = I1.intersection(I2)
        if inter == I1 or inter == I2:
            cnt+=1

    
    #part 2
    cnt2 = 0
    for l in tab_f:
        p1,p2 = l.split(",")
        p1 = p1.split("-")
        p2 = p2.split("-")
        p1[0] = int(p1[0])
        p1[1] = int(p1[1])
        p2[0] = int(p2[0])
        p2[1] = int(p2[1])
        
        m_c = 0
        m_c2 = 0
        print(l)
        if p1[1] >= p2[0] and p1[0]<=p2[1]:
            cnt2+=1
    
        I1 = set([i for i in range(p1[0],p1[1]+1)])
        I2 = set([i for i in range(p2[0],p2[1]+1)])
        inter = I1.intersection(I2)
        #if len(inter) > 0:
            #print("i_check")

        print()
print(cnt)
print(cnt2)
