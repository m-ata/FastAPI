from math import factorial


number = int(input("Enter an Number to calculate Factorial : "))

factorial=1

while number >0 :
    factorial =  factorial * number
    number = number -1

print(factorial)