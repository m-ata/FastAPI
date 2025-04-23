import time

def timer(func):
    
    def wrapper (*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print (f"{func.__name__}  ran in {end-start} seconds.")
        return result
    
    return wrapper



# custom Decorator 
@timer
def example_function (n):

    time.sleep(n)
    return print(f"Sleep for {n} seconds")
example_function(4)