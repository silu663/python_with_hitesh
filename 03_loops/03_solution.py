# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration

input_number = int(input('enter the number for which you want the multiplication table')
)

for num in range(1,11) :
    if num == 5:
        continue
    else:
        print(f'{input_number} X {num} = {input_number * num}')



     