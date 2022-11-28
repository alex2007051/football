a, b = map(int, input().split())

roads = {}
for i in range(a - 1):
    r, k, e = map(int, input().split())
    roads[(r, k)] = e

skla = []
for i in range(b):
    skla.append(int(input()))

mar = {}
for i in roads:
    if i[0] not in mar:
        mar[i[0]] = []
    mar[i[0]].append(i[1])
    if i[1] not in mar:
        mar[i[1]] = []
    mar[i[1]].append(i[0])

marchru = []



    


















































