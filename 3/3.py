#modular solution for parts 1 and 2, just adjust the "N" variable from 2 -> 12
def soln(N):
    lines = [[char for char in i.strip()] for i in open("3.txt", "r").readlines()]
    sum = 0
    for rating in lines:
        digits = []
        line = rating
        for depth in range(1,N+1):
            n=line.index((max(line[:-(N-depth)])) if depth < N else max(line))
            digits.append(line[n])
            line = line[n+1:]
        sum+=int("".join(digits))
    return sum

print(soln(2))
print(soln(12))