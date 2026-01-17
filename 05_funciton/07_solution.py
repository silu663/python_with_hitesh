# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    print('args = ',args)
    print('*args = ',*args)
    
    return sum(args)

print(sum_all(1,2,3))