#1. Function Defination is one time proces
def multiplicationThreeNumber(a, b, c):  #a,b,c id formalargument
    multiplication_result = a * b * c
    print(f'The Product of {a}, {b} and {c} is: {multiplication_result} ')

#2. Function calling/invoking is many time process
multiplicationThreeNumber(b=6, c=2, a=9)  #a,b,c is actualargument    