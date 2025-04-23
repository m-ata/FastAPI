

age = int(input("Enter an age : "))
# print(type (age))
day = str(input("Enter a day : "))
discount=2

price = 12 if  age>=18 else 8
discount = 2 if day=='wed' else 0

if age < 18:
    print("Child")
    print("Price of ticket will be : " , price-discount ,"$")
elif (age>=18 and age <25):
    print("Teen")
    print("Price of ticket will be : " , price-discount  ,"$")
else:
    print("Younger")
    print("Price of ticket will be : " , price-discount  ,"$")

