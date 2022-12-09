win = {"A" : "B", "B" : "C", "C" : "A"}
lose = {"A" : "C", "B" : "A", "C" : "B"}
scoring = {"A" : 1, "B" : 2, "C" : 3}

with open("input_day2.txt","r") as f:
    tab_f = f.read().splitlines()
    total = 0
    for l in tab_f :
        score = 0
        Ennemy, Player = l.split(" ")
        
        if Player == "X" :
            score += 1
            if Ennemy == "C" :
                score += 6
            if Ennemy == "A" :
                score += 3
        
        if Player == "Y" :
            score += 2
            if Ennemy == "A" :
                score += 6
            if Ennemy == "B" :
                score += 3
                
        if Player == "Z" :
            score += 3
            if Ennemy == "B" :
                score += 6
            if Ennemy == "C" :
                score += 3
        
        total += score
        
    # PART 2
    print("part 1 : " + str(total))
    
    total = 0
    
    for l in tab_f :
        score = 0
        Ennemy, Player = l.split(" ")
        Played = "_"
        if Player == "X" :
            Played = lose[Ennemy]
        if Player == "Y" :
            Played = Ennemy
            score += 3
        if Player == "Z" :
            Played = win[Ennemy]
            score += 6
        score += scoring[Played]
        total += score
    
    print("part 2 : " + str(total))

