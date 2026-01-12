# Problem: Keep asking the user for input until they enter a number between 1 and 10

user_input = input('enter a number between 0 to 10 \n')


valid_string = '0 1 2 3 4 5 6 7 8 9 10'

while not user_input in valid_string :
    user_input = input('❌❌❌ enter again ❌❌❌ \n')

print('SUCCESSFUL✅✅✅✅✅')
