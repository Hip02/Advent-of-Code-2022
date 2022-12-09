
with open("input_day3.txt","r") as f:
    tab_f = f.read().splitlines()
    sum = 0
    c = 0
    for l in tab_f:
        c += 1
        l1,l2 = l[0:len(l)//2], l[len(l)//2:len(l)]
        s1,s2 = set(l1), set(l2)
        inter = ""
        val = 0
        for i in s1.intersection(s2):
            inter = i
        if i.isupper():
            val = ord(i)-38
        else :
            val = ord(i)-96

        sum += val


    sum2 = 0
    for l in range(0, len(tab_f), 3):

        c += 1
        l1,l2,l3 = tab_f[l], tab_f[l+1], tab_f[l+2]
        s1,s2,s3 = set(l1), set(l2), set(l3)
        inter = ""
        val = 0
        for i in s1.intersection(s2).intersection(s3):
            inter = i
        if i.isupper():
            val = ord(i)-38
        else :
            val = ord(i)-96

        sum2 += val

print()
print(sum)

print("PART 2")

print(sum2)



