

from ast import arg


def print_args(func):
    def wrapper(*args,**kwargs):
        # print(f"{func.__name__} , Arguments : {(", ").join(f"{key} : {value}" for key, value in dict(args))}")
        print(f"{func.__name__} , Arguments : {(", ").join(f"{arg} " for arg in args)}")
        return func(*args,**kwargs)
        
    return wrapper


@print_args
def CarDetails(name, model, spec):
    spec_details = ", ".join(f"{key}: {value}" for key, value in spec.items())
    return f"Car: {name}, Model: {model}, Specs: {spec_details}"

print(CarDetails("Toyota", 2016, {"Battery": "5000mAh", "Color": "Black"}))
