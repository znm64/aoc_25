def inrange(pos, max):
    if pos < max and pos >=0:
        return True
    else:
        return False
raw = [[j for j in i.strip()] for i in open("4.txt", "r").readlines()]
xlen = len(raw[0])
ylen = len(raw)

def scan(raw):
    remove = []
    for y, row in enumerate(raw):
        for x, sym in enumerate(row):
            rolls = 0
            if sym == "@":
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        xpos,ypos = x+dx,y+dy
                        if (dx==0) and (dy==0):
                            continue
                        if inrange(xpos, xlen) and inrange(ypos, ylen):
                            if raw[ypos][xpos] == "@":
                                rolls += 1                                
                if rolls < 4:
                    remove.append((x,y))
    return remove

final = 0    
while True:
    map = raw
    remove = scan(raw)
    final+=len(remove)
    if len(remove)==0:
        break
    for i in remove:
        #print(i)
        #print(type(i[1]), type(i[0]))
        map[int(i[1])][int(i[0])] = "."
    
print(final)