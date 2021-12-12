class Users:

    def __init__(self, first_name, last_name,user_name,e_mail,location):
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.e_mail=e_mail
        self.location=location

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.user_name}")
        print(f"Email: {self.e_mail}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.user_name}!")

andrei = Users('andrei','cop','e-cop','e-cop@gmail.com', 'quebec')
andrei.describe_user()

ivan = Users('ivan', 'groznii', 'grozniiIvan', 'groznii@live.ca', 'Montreal')
ivan.describe_user()

