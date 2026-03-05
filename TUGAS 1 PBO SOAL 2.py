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

print(f"The reastaurant name is {restaurant1.restaurant_name}")
print(f"This restaurant offers {restaurant1.cuisine_type} cuisine.")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print( )

restaurant2 = Restaurant("La Tavola", "Italian")

print(f"The reastaurant name is {restaurant2.restaurant_name}")
print(f"This restaurant offers {restaurant2.cuisine_type} cuisine.")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
print( )

restaurant3 = Restaurant("El Rancho", "Mexican")

print(f"The reastaurant name is {restaurant3.restaurant_name}")
print(f"This restaurant offers {restaurant3.cuisine_type} cuisine.")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
