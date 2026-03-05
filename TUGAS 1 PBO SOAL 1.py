class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

restaurant1 = Restaurant("Warung Mak Beng", "Indonesian")

print(f"The restaurant name is {restaurant1.restaurant_name}")
print(f"This restaurant offers {restaurant1.cuisine_type} cuisine.")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()