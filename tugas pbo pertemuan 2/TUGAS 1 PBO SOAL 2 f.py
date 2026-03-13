# soal 2
""" Dari soal nomor 1, buatlah 3 instance berbeda dari kelas tersebut, dan panggil describe_restaurant() untuk setiap instance. """


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type}")

restaurant1 = Restaurant("Sederhana", "Masakan Padang")
restaurant2 = Restaurant("Pizza Hut", "Pizza")
restaurant3 = Restaurant("Bakso Beranak", "Bakso")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
