#  Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car)

distance = int(input('enter the travellig distance ? :')
)

if distance < 3 :
    transport = "Walk"
elif distance <= 15 :
    transport = "Bike"
else :
    transport = "Car"

print('Go for a',transport)

    