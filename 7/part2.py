def locate(a:str,b:str)->list[int]:
    c=[]
    for n,i in enumerate(a):
        if i==b:
            c.append(n)
    return c

raw = [i.strip() for i in open("7.txt","r").readlines()]

width=len(raw[0])

groups = [0 for i in range(width)]
groups[raw[0].index("S")]=1
rows = raw[1:]
total=0
carets = [locate(row,"^") for row in raw[1:]]
carets=carets[1::2]

#input cleaning done

#strategy:
#track every path and discard almost all information
#just tally how many paths are at each x coordinate at any time
paths = [[raw[0].index("S")]]
for n,row in enumerate(carets):
    print(n)
    newgroups = groups[:]
    for caret in row:
    
        newgroups[caret+1]+=(groups[caret])
        newgroups[caret-1]+=(groups[caret])
        newgroups[caret]=0

    groups=newgroups[:]

print(sum((group) for group in groups))