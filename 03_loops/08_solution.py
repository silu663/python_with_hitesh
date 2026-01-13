# Problem: Check if a number is prime.
input_number = int(input('enter a number ? :'))
count = 0

for num in range(1,input_number+1) :
    if input_number % num == 0 :
        count += 1


if count == 2 :
    print(f'{input_number} is a prime number')
else :
    print(f'{input_number} is not a prime number')

        