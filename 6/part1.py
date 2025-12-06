raw = open("6.txt", "r").readlines()
values = [ i.strip().split() for i in raw[:-1]]
operations = raw[-1].strip().split()
total=0
for x in range(len(values[0])):
    calculation = values[0][x]
    operation = operations[x]
    nums = [values[y][x] for y in range(1, len(values))]
    for y in range(1, len(values)):
        calculation+=(operation+values[y][x])
    total+=(eval(calculation))
print(total)