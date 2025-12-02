#strip zeroes, then check for repeats 
raw = open("2.txt", "r").read().strip().split(",")
total=0

for a in raw:
    b = [int(x) for x in a.split("-")]
    for id in range(b[0], b[1]+1):
        id=str(id)
        if len(id)%2 == 0:
            if id ==2*id[:int(len(id)/2)]:
                total += int(id)

print("\n"+str(total))

#part 2
total=0
collections = set()
for a in raw:
    b = [int(x) for x in a.split("-")]
    for id in range(b[0], b[1]+1):
        id=str(id)
        for i in range(1,len(id)):
            sub = id[:i]
            if (len(id)%len(sub)) == 0:
                sub = id[:i]
                if id == ((int(len(id)/len(sub))*sub)):
                    collections.add(int(id))

for id in collections:
    total+=id
print("\n"+str(total))