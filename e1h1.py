from math import sin, radians
def area(a, b , angle):
    return 0.5*a*b*sin(radians(angle))

print(area(1,2,30))
