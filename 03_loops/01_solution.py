# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_num_count = 0
positive_num = []
for num in numbers :
    if num % 2 == 0 :
        positive_num.append(num)
        positive_num_count += 1
        
print('positive number = ',positive_num_count,positive_num)


    
    
