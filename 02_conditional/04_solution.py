import string
input_string = input("what is the colour of the fruit?").lower()

# special_characters = string.punctuation
# numbers = "1234567890"

# if " " in input_string :
#     input_string = input_string.replace(" ","")

# for char in special_characters :
#     if char in input_string :
#         input_string = input_string.replace(char,"")

# for num in numbers :
#     if num in input_string :
#         input_string = input_string.replace(num,"")
# above are the optional checking

      
Fruit_color = input_string

if Fruit_color == "green" :
    print('Fruit is unripe')
elif Fruit_color == "yellow" :
    print('Fruit is ripe')
elif Fruit_color == "brown" :
    print('Fruit is over ripe')
else :
    print('Fruit is use less')
    
    








