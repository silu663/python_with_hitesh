# Problem: Compute the factorial of a number using a while loop

input_number = int(input('enter the numbe for which you want to calculate the factorial  ?\n')
)

factorial = 1

# for num in range(1,input_number +1):
#     factorial *= num

while input_number >0 :
    factorial *= input_number
    input_number -=1
    
print('factorial is ',factorial)
