import math

T = 10
t =0
v = 1
cords = []
while t  <= 10:
    r = v * t
    x = r * math.sin(2 * math.pi * t / T)
    y = r * math.cos(2 * math.pi * t / T)
    cords.append([x ,y ])
    t += 0.5
odg = 0
for i in range(len(cords)-1):
    A = cords[i]
    B = cords[i+1]
    x1 = 0
    x2 = 0
    y1  = 1
    y2 = 1
    accodg = ((B[x2]- A[x1])**2 + (B[y2]- A[y1])**2)**0.5
    odg+=accodg
print(round(odg, 4 ))
print(cords)
