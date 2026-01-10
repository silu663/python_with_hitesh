age = int(input("enter the age ?"))
day = "wednes"

# if day == "wednes" :
#     price = (12 - 2) if age >= 18 else (8 - 2)
# else :
#     price = 12 if age >= 18 else 8

price = 12 if age >= 18 else 8

if day == "wednes" :
    price -= 2



print("your ticket price is $",price)

