instructions = [(int(i[0]=="R"), int(i[1:].strip())) for i in open("1.txt", "r").readlines()]


n=50
c = 0 
for line in instructions:
    n = (n+(line[1]*(line[0]*2 - 1)))%100
    if n == 0:
        c += 1
print(c)

# part 2
n=50
c = 0 
for line in instructions:
    for i in range(line[1]):
        n = (n+(line[0]*2 - 1))%100
        if n == 0:
            c += 1
print(c)