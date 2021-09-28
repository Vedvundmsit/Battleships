ship = [ [0, 0], [1, 0], [3, 0] ]
colCond = True
seqCond = True

for i in range(len(ship)):
    if ship[0][1] != ship[i][1]:
        colCond = False

rows = [ ]
for i in range(len(ship)):
    rows.append(ship[i][0])
rows.sort()

for i in range(len(ship)-1):
    if 1+rows[i] != rows[i+1]:
        seqCond = False

if colCond:
    if seqCond:
        print("all ok")