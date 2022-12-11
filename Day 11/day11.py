class Monkey:
    def __init__(self, items, operation, test, throws):
        self.items = items
        self.operation = operation
        self.test = test
        self.throws = throws
        self.inspect_count = 0

monkeys = []
rounds = 10000

def get_n_most_inspectors(n,monkeys):
    l = []
    for monkey in monkeys:
        l.append(monkey.inspect_count)
    return sorted(l)[-n:]

def show_inspect_counts(monkeys):
    for i,monkey in enumerate(monkeys):
        print(f"Monkey[{i}] has inspected {monkey.inspect_count} items")

def show_items(monkeys):
    for i,monkey in enumerate(monkeys):
        print(f"Monkey[{i}] has {monkey.items}")

def apply_operation(operation, x):
    ops = operation.split()
    x1 = int(ops[0]) if ops[0] != "old" else x
    x2 = int(ops[2]) if ops[2] != "old" else x
    return x1 + x2 if ops[1] == "+" else x1 * x2

def get_product_primes_monkey(monkeys):
    r = 1
    for monkey in monkeys:
        r *= monkey.test
    return r
    
with open("input_day11.txt","r") as f:
    tab_f = f.read().splitlines()
    for i in range(0,len(tab_f),7):
        items = [int(j) for j in  tab_f[i+1].split(":")[1].split(",")]
        operation = tab_f[i+2].split("=")[1]
        test = int(tab_f[i+3].split()[-1])
        throws = (int(tab_f[i+4].split()[-1]),int(tab_f[i+5].split()[-1]))
        monkey = Monkey(items,operation,test,throws)
        monkeys.append(monkey)
        
toModulo = get_product_primes_monkey(monkeys)

for r in range(rounds):
    #print(r)
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        while(len(monkey.items) > 0):
            monkey.inspect_count += 1
            item = monkey.items.pop(0)
            item_op = apply_operation(monkey.operation, item)
            #item_op //= 3
            t = ((item_op % monkey.test) == 0)
            item_op %= toModulo
            #else : item_op = ((item_op // monkey.test) + (item_op % monkey.test))
            m = monkey.throws[0] if t else monkey.throws[1]
            monkeys[m].items.append(item_op)
    #print(f"After round {r+1}")
#show_items(monkeys)
#print()
    
show_inspect_counts(monkeys)
most_inspected = get_n_most_inspectors(2, monkeys)
result = 1
for n in most_inspected :
    result *= n
print(result)
    

    
    
        