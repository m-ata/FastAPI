class Car():
    def __init__(self , model , name) :
        self.model=model
        self.name=name
    
    def full_name(self):
        return f"Car Model: {self.model} . \nCar Name : { self.name} ."


my_car = Car("Toyota", "Corolla")
# print(my_car)
# print(my_car.model)
# print(my_car.name)
print(my_car.full_name())