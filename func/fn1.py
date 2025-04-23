

# lambda fucntion ( no name of the function)

cube  = lambda x: x **3

print(cube(3))

# deafault params 

name  = lambda x="Nabeel": x

print(name("User"))

# Multiple parameters with - *args

def sum_all(*args):
    print(args) # (tuple)
    # print(type(args)) # tuple
    print(*args)  # single elements of tuple
    print(sum(args))


print("-------------------")
sum_all(1,2,3)


# When handling key values paris in fucntion we need to use **kwargs

def  print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} - {value} pairs of living things..")

print_kwargs(male="human", female="women") 
print_kwargs(male="parrot", female="pigeon") 



