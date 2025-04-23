

# prime = False 
# number = int(input("Enter an number : "))

# if number > 0 :
#     for i in range ( 2 , number):
#         if (number % 2 )==0:
#             prime= True
#             break

# print(f"The number is {"Prime" if prime==True else  "No Prime"}")

chars =[ 1,3,4,5,7,2,4,2,4]
newChars = []

for i in chars:
    if i in newChars:
        continue
    else :
        newChars.append(i)
        newChars.sort()
        
print(f"The list of unique Items is {newChars}")