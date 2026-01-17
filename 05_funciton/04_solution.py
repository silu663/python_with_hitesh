# Problem: Create a function that returns both the area and circumference of a circle given its radius

import math

radius = 7

def area_and_circumference(radius):
    pi = math.pi
    area = pi * (radius ** 2)
    circumference = 2 * pi * radius
    return area,circumference


(area,circumference) = area_and_circumference(radius)

# print('result',result[0])
# print('type of result',type (result))

print('area',area)
print('circumference ',circumference)




