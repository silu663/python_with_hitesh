# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# learning about the kwargs
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')
        


print_kwargs(name = "Thor" , power = "StromBreaker" ,enemy = "Thenos")
print_kwargs(name = "Brus Banner" ,wife = "Natasa",degree = "126 PHds")
print_kwargs(name = "Iron Man")
print_kwargs(power = "Black Book",name = "wanda")