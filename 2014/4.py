import math

T = 12.5
t =3
r = 5
x = r * math.sin(2*math.pi*t/T)
y = r * math.cos(2*math.pi*t/T)
while y <x:
    t += 0.05
    x = r * math.sin(2 * math.pi * t / T)
    y = r * math.cos(2 * math.pi * t / T)

print(round(t,3))
