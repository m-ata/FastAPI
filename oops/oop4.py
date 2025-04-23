class Car():
    def __init__(self, model: str, name: str):
        self.__model = model   # private variable
        self.name = name
    
    def full_name(self):
        return f"Car Model: {self.__model}.\nCar Name: {self.name}."

    # GETTER function
    def get_model(self):
        return self.__model

    # SETTER function
    def set_model(self, value):
        if value:
            self.__model = value
            return self.__model
        else:
            return "Invalid model name."


# Inheritance with super() to access parent class
class Electric_Car(Car):
    def __init__(self, model, name, battery_size: int):
        super().__init__(model, name)
        self.battery_size = battery_size

    def private_full_eCar_details(self):
        model_name = self.get_model()
        return f"***Private Details***\nCar Model: {model_name}.\nCar Name: {self.name}.\nBattery Size: {self.battery_size} KWh."

    def private_full_eCar_details_with_setter(self, model_value, name_value):
        model_name = self.set_model(model_value)
        self.name = name_value
        return f"***Private Details with Setting***\nCar Model: {model_name}.\nCar Name: {self.name}.\nBattery Size: {self.battery_size} KWh."


# Testing the class
my_eCar = Electric_Car("Tesla", "Tesla Truck", 5000)
print(my_eCar.private_full_eCar_details())
print(my_eCar.private_full_eCar_details_with_setter("Royal Royce", "Lamborghini"))
