raw =[i.strip("\n") for i in  open("6.txt", "r").readlines()]
operations = raw[-1].strip().split()
total=0

spaces = []
positions = []
for row in raw[:-1]:
    a=set()
    for count, i in enumerate(row):
        if i==" ":
            a.add(count)
    positions.append(a)

spaces = set.intersection(*positions)
spaces=sorted(list(spaces))
values=[]
for row in raw[:-1]:
    temp = [row[:spaces[0]]]
    for count, pos in enumerate(spaces):
        if count==0:
            continue
        temp.append(row[spaces[count-1]:pos])
    temp.append(row[spaces[-1]:])
    values.append(temp)


for x in range(len(values[0])):
    group = [row[x] for row in values]
    maxlen = max([len(i) for i in group])
    exp=[]
    op = operations[x]
    for i in range(maxlen):
        for y in range(len(group)):
            char= group[y][i]
            if char!=" ":
                exp+=(char)
        exp+=op
    exp=exp[:-1]
    if not exp[0].isalnum():
        exp=exp[1:]
    exp = ("".join(exp))
    total+=eval(exp)
print(total)