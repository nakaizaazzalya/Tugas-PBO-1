# soal 1
"""    1.	Buat kelas bernama Restaurant. Metode __init__() untuk Restaurant harus menyimpan dua atribut: 
nama restoran (restaurant_name) dan jenis masakan (cuisine_type). Buatlah metode bernama describe_restaurant() 
yang mencetak kedua informasi ini, dan metode bernama open_restaurant() yang mencetak pesan yang menunjukkan 
bahwa restoran tersebut buka. Buat instance bernama restaurant dari kelas Anda. Cetak kedua atribut tersebut
 secara terpisah, lalu panggil kedua metode tersebut."""


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

restaurant1 = Restaurant("Sederhana", "Masakan Padang")

print(f"The restaurant name is {restaurant1.restaurant_name}")
print(f"This restaurant offers {restaurant1.cuisine_type}")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()