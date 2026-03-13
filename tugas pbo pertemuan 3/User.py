class User:
    def __init__(self, first_name, last_name, age, email, city
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.email = email
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name  : {self.first_name} {self.last_name}")
        print(f"Age   : {self.age}")
        print(f"Email : {self.email}")
        print(f"City  : {self.city}")

    def greet_user(self):
          print(f"Hello {self.first_name}, welcome back!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0