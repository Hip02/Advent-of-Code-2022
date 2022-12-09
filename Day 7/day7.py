class Node(object):
    class_counter = 0
    def __init__(self, name, parent=None, size=None, id=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []
        self.id = Node.class_counter
        Node.class_counter += 1

    def add_child(self, obj):
        self.children.append(obj)

database = {'root':[]}

Root = Node('root')

with open("input_day7.txt","r") as f:
    tab_f = f.read().splitlines()
    tab_f.append('END')
    current_node = Root
    for i in range(len(tab_f)):
        #print(f'line[{i}] : pwd = {pwd}')
        line = tab_f[i]
        cmd = line.split()
        if cmd[0] == '$' :
            if cmd[1] == 'cd' :
                if cmd[2] == '/' :
                    while current_node.parent != None:
                        current_node = current_node.parent
                elif cmd[2] == '..' :
                    current_node = current_node.parent
                else :
                    found = False
                    for child in current_node.children :
                        if child.name == cmd[2] :
                            current_node = child
                            found = True
                            break
                    if found == False :
                        child = Node(cmd[2], current_node)
                        current_node.add_child(child)
                        current_node = child
                        
            elif cmd[1] == 'ls' :
                j = 1
                current_ls = current_node.children
                while tab_f[i+j][0] != '$' and tab_f[i+j] != 'END':
                    line_out = tab_f[i+j]
                    #print(f"{line_out} being added to {pwd[-1]}")
                    out = tab_f[i+j].split()
                    id = str(i+j)
                    if out[0] == 'dir' :
                        child = Node(out[1], current_node)
                        current_node.add_child(child)
                    else :
                        child = Node(out[1], current_node, int(out[0]))
                        current_node.add_child(child)
                    j += 1
                i += j

def print_tree(node):
    print(f"{node.name}")
    for c in node.children : print_tree(c) 

#print_tree(Root)

dir_size = {}

def look_size(node):
    size = 0
    if node.size == None:
        for child in node.children :
            size += look_size(child)
        dir_size[node.name+str(node.id)] = size
        return size
    else :
        return node.size

look_size(Root)

print(dir_size)

total_size = 0
for k,v in dir_size.items():
    if v <= 100000:
        total_size += v
        print(f"{k} has {v}")
    
print(f"total size = {total_size}")

total_disk = 70000000
unused_disk = 30000000
root_disk = dir_size['root0']
must_have_disk = total_disk - root_disk
required = unused_disk - must_have_disk

OK_dir = []

for k,v in dir_size.items():
    if v >= required :
        OK_dir.append(v)

OK_dir.sort()

print(OK_dir)

# def look_size(dir):
#     try :
#         files_size = 0
#         ls = database.get(dir,[])
#         for item in ls :
#             if(item[0] == 'dir'):
#                 files_size += look_size(item[1])
#             else:
#                 files_size += item[2]
#         return files_size
#     except :
#         print(f"error with {dir}")

#print()
#print(database['dcqnblb'])

#total_size = 0
#for k in database.keys():
#    size = 0#look_size(k)
#    if size < 100000:
#        total_size += size
#        #print(f"{k} has {size}")
    
#print(f"total size = {total_size}")