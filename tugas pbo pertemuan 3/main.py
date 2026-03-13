from restaurant import Restaurant

restaurant1 = Restaurant("Sederhana", "Masakan Padang")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print("Jumlah pelanggan awal:", restaurant1.number_served)

restaurant1.set_number_served(20)
print("Jumlah pelanggan setelah diubah:", restaurant1.number_served)

restaurant1.increment_number_served(5)
print("Jumlah pelanggan setelah ditambah:", restaurant1.number_served)
