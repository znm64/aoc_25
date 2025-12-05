raw = open("5.txt","r").read().split("\n\n")
ranges = [[int(j) for j in i.split("-")] for i in raw[0].split("\n")]
values = [int(j) for j in raw[1].split()]
total=0
for value in values:
    success = False
    for range in ranges:
        if (range[0]<=value<=range[1]):
            success = True
            break
    if success:
        total+=1

print(total)