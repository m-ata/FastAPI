class Car():

    # class variables 
    total_objects_ceated_by_parent_obj = 0

    def __init__(self, model: str, name: str):
        self.__model = model
        self.name = name

        # when times call but this modify the instance 
        self.total_objects_ceated_by_parent_obj += 1

        # when times call but this track the instance created 
        Car.total_objects_ceated_by_parent_obj += 1
    def full_name(self):
        return f"Car Model: {self.__model}.\nCar Name: {self.name}."

    def get_model(self):
        return self.__model

    def set_model(self, value):
        if value:
            self.__model = value
            return self.__model
        else:
            return "Invalid model name."


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


my_eCar = Car("Tesla", "Tesla Truck")
my_eCar2 = Car("Royal Royace", "Lubergnee")
my_eCar3 = Car("Ferari", "Hosei")

print(Car.total_objects_ceated_by_parent_obj)

# print(my_eCar3.total_objects_ceated_by_parent_obj)