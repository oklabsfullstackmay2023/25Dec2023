#1. Function Defination is one time process
def substractionThreeNumber(x, y, z):   #x, y, z is formalargument
    substraction_result = x - y - z
    print(f'The difference of {x}, {y}, and {z} is: {substraction_result}')

#2. Function calling/invoking is many time process
substractionThreeNumber(y=45, z=35, x=15)  #y, z, x is actualargument
