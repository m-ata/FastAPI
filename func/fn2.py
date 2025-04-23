number = (int(input("Enter a number of Yeild to generate Prime Numbers : ")))
prime_nums=[]
def gen_prime(number):
    if number <=0:
        print("wrong Number")
        exit()
    else:
        for i in range(2 , number):
            num = i % 2 ==0
            prime_nums.append(i) if num==True  else ""

        print(prime_nums)

gen_prime(number)


