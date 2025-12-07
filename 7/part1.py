def locate(a:str,b:str)->list[int]:
    c=[]
    for n,i in enumerate(a):
        if i==b:
            c.append(n)
    return c

raw = [i.strip() for i in open("7.txt","r").readlines()]

positions = set()
positions.add(raw[0].index("S"))

rows = raw[1:]
total=0
carets = [locate(row,"^") for row in raw[1:]]
for i in carets:
    for point in i:
        if point in positions:
            total+=1
            positions.discard(point)
            positions.add(point+1)
            positions.add(point-1)
            
print(total)