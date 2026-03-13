# soal 3
"""3.	Buatlah kelas bernama User. Buat dua atribut bernama first_name dan last_name,
 lalu buat beberapa atribut lain yang biasanya disimpan dalam profil User. Buat metode
bernama describe_user() yang mencetak ringkasan informasi pengguna. Buat metode lain 
bernama greet_user() yang mencetak salam pribadi kepada user. Buatlah beberapa instance 
yang mewakili user yang berbeda, dan panggil kedua metode tersebut untuk setiap user."""


class User:
    """Model sederhana untuk merepresentasikan user."""

    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print(f"Name  : {self.first_name} {self.last_name}")
        print(f"Age   : {self.age}")
        print(f"Email : {self.email}")
        print(f"City  : {self.city}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

user1 = User("Nakaiza", "Azzalya", 20, "nakaiza@gmail.com", "Jakarta")
print(f"The user's name is {user1.first_name} {user1.last_name}")
print(f"This user lives in {user1.city}")
user1.describe_user()
user1.greet_user()
print()

user2 = User("Siti", "Nayla", 22, "siti@gmail.com", "Bandung")
print(f"The user's name is {user2.first_name} {user2.last_name}")
print(f"This user lives in {user2.city}")
user2.describe_user()
user2.greet_user()
print()

user3 = User("Dzul", "Hannan", 21, "hannan@gmail.com", "Surabaya")
print(f"The user's name is {user3.first_name} {user3.last_name}")
print(f"This user lives in {user3.city}")
user3.describe_user()
user3.greet_user()