
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print('Name', self.name)
        print('Age', self.age)
        print('Gender', self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.amount = None
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        return 'Account updated '+ str(self.balance)

    def wihdrawal(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficient Balance')
        else:
            self.balance = self.balance - self.amount
            print('Account updated', self.balance)

    def view_details(self):
        self.show_details()
        print('Account balance', self.balance)



Mohit = Bank('Mohit', 21, 'Male')
print(Mohit.deposit(10))


