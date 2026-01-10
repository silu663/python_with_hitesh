# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
weather = input('enter the weather condition ex- sunny,rainy,snowy \n :').lower()


if weather == "sunny" :
    activity = "go for a walk"
elif weather == "rainy":
    activity = "read a book"
elif weather == "snowy" :
    activity = "Build a snowman"

print('activity',activity)

    