#1.Function Defination is one time process
def calculateThreeNumber(x, y, z):# x, y and z is formalargument    
    addition_result= x + y + z
    print(f'The sum of {x}, {y} and {z}: {addition_result} ')  

#2.Function calling/invoking is many time process
calculateThreeNumber(z=15, y=30, x=45)#z, y and x is actualargument

    