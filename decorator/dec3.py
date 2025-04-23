import time



def cache(fucn):
    cache_memory={}
    def wrapper(*args , **kwargs):
        if args in cache_memory:
            return cache_memory[args]
        result = fucn(*args,**kwargs)
        cache_memory[args] = result 
        print(cache_memory) # saving in to the cache
        return result
    return wrapper

@cache
def example(n, a, b):
    print("function running")
    time.sleep(n)
    return  a+b

print("SUM : ",example(3, 2, 5))
print("SUM : ",example(3, 2, 5))
