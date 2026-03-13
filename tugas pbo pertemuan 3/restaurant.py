class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self,  customers):
        self.number_served += customers