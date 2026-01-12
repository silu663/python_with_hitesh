# Problem: Given a string, find the first non-repeated character.

input_string = "teeterrHHjjkwoppp"

for char in input_string :
    if input_string.count(char) == 1 :
        print(f'the first non reapeted character is {char}')
        break
        
