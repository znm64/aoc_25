def inrange(pos, max):
    if pos < max and pos >=0:
        return True
    else:
        return False
    
raw = [i.strip() for i in open("4.txt", "r").readlines()]
total = 0
xlen = len(raw[0])
ylen = len(raw)
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
                total+= 1         
print(xlen,ylen)
print(total)