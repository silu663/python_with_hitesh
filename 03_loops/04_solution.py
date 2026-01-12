# Problem: Reverse a string using a loop
input_string = input('enter the string you want to reverse ? \n')

char_list =[]
for char in input_string :
    char_list.append(char)

char_list.reverse()

reversed_string = ''.join(char_list)
print('reversed string is ',reversed_string)


    