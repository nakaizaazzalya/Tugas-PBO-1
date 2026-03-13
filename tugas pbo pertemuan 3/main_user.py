from User import User

user = User("Nakaiza", "Azzalya", 20, "nakaiza@gmail.com", "Jakarta")

user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Jumlah login attempts: {user.login_attempts}")

user.reset_login_attempts()

print(f"Login attempts setelah reset: {user.login_attempts}")