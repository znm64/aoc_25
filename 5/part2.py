raw = open("5.txt","r").read().split("\n\n")
ranges = [[int(j) for j in i.split("-")] for i in raw[0].split("\n")]
points = []
for range in ranges:
    points.append((range[0], 0, range[1]))
    points.append((range[1],1, -1))

points.sort(key=lambda point:(point[0]+(point[1]/2)))

total=0
state=1
started_at = points[0][0]
dont_end_before = points[0][2]
for i in points[1:]:
    if state:
        if i[2] > dont_end_before:
            dont_end_before = i[2]
        if i[1]==1:
            if i[0]<dont_end_before:
                continue
            state=0
            total+=(1+i[0]-started_at)
    if not state:
        if i[1]==0:
            state=1
            started_at = i[0]
            dont_end_before = i[2]

print(total)