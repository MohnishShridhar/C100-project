class Card(object):

    def __init__(self, name, number, pin, amount):
        self.name=name
        self.number=number
        self.pin=pin
        self.amount=amount

    def withdraw(self):
        amt= input("How much do you want to withdraw: ")
        print("withdrawn " + amt)

    def know(self):
        print(self.amount)

card1=Card("card1", "0000000000", "0000", 80)
print(card1.know())