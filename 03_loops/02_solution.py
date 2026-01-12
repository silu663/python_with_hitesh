# Problem: Calculate the sum of even numbers up to a given number n
limit = int(input('enter the number till you want to sum of the even numbers ?')
)

summation_of_even_number = 0

for num in range(0,limit+1):
    if num % 2 == 0:
        summation_of_even_number += num

print('summation is ',summation_of_even_number)
