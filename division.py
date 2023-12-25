#1. Function Defination is one time process
def divisionThreeNumber(x, y, z):  #x,y,z is formalargument
    division_result = x / y / z 
    print(f'The Division of {x}, {y} and {z} is: {division_result} ')

#2. Function calling/invoking is many time process
divisionThreeNumber(y=5, x=25, z=3)    