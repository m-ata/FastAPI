class Car():
    def __init__(self , model:str , name:str) :
        self.model=model
        self.name=name
    
    def full_name(self):
        return f"Car Model: {self.model} . \nCar Name : { self.name} ."

# Inheritance with super power of the parent class
# calling __init__ with super to call get the attributes of the parent class
class Electric_Car(Car) :
    def __init__(self, model, name , battery_size:int ):
        super().__init__(model, name)
        self.battery_size = battery_size

    def full_eCar_details(self):
        return f"Car Model: {self.model} .\nCar Name : { self.name} .\nBattery Size : { self.battery_size} Kwh ."


my_eCar =(Electric_Car("Tesla", "Tesla Truck",5000)) 
print(my_eCar .full_eCar_details()) 