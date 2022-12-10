cycle_cnt = 0
current_value = 1
important_register = []

screen = [[" " for j in range(40)] for i in range(6)]

def print_screen(screen):
    for line in screen:
        print("".join(line))

with open("input_day10.txt","r") as f:
    tab_f = f.read().splitlines()
    for line in tab_f:
        instruction = line.split()

        for i in range(2):
            if cycle_cnt%40 in [current_value-1,current_value,current_value+1]:
                screen[cycle_cnt//40][cycle_cnt%40] = "#"
            if (cycle_cnt+1 - 20) % 40 == 0 :
                important_register.append((cycle_cnt+1)*current_value)
            cycle_cnt += 1
            if instruction[0] == 'noop':
                break
            else :
                if i == 1 :
                    current_value += int(instruction[1])
                    
            
print(important_register)
print(sum(important_register))
print_screen(screen)