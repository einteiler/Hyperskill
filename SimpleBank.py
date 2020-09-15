import random
import sqlite3

conn = sqlite3.connect('card.s3db')
with conn:
    conn.execute('''CREATE TABlE IF NOT EXISTS card (
                               id       INTEGER PRIMARY KEY AUTOINCREMENT,
                               number   TEXT,
                               pin      TEXT,
                               balance  INTEGER DEFAULT 0);''')

class SimpleBank:

    iin = '400000'
    checksum = '0'
    
    def __init__(self, connector):
        self.cursor = connector.cursor()
        self.choice = 0

    def db_check(self, column, value):
        command = f'SELECT {value} FROM card WHERE {column} = {value}'
        self.cursor.execute(command)
        return self.cursor.fetchone()

    def acc_number(self, digits=9):
        return ''.join((random.choice('1234567890') for i in range(digits)))

    def find_checksum(self, customer):
        total = 0
        digit_list = [int(x) for x in customer]
        for i in range(0, len(digit_list), 2):
            digit_list[i] *= 2
            if digit_list[i] > 9:
                digit_list[i] -= 9
        for x in digit_list:
            total += x
        return str((10 - total % 10) % 10)

    def create(self):
        account = self.acc_number()
        customer = self.iin + account
        self.checksum = self.find_checksum(customer)
        customer += self.checksum
        pin = self.acc_number(4)
        balance = 0
        self.cursor.execute(f'SELECT * FROM card WHERE number = {customer}')
        if self.cursor.fetchone():
            self.create()
        else:
            self.cursor.execute(f'INSERT INTO card (number, pin) VALUES ({customer}, {pin})')
            conn.commit()
            print(f"""Your card has been created\nYour card number:\n{customer}\nYour card PIN:\n{pin}""")

    def luhn(self, card):
        total = 0
        digit_list = [int(x) for x in card]
        for i in range(0, len(digit_list), 2):
            digit_list[i] *= 2
            if digit_list[i] > 9:
                digit_list[i] -= 9
        for x in digit_list:
            total += x
        return total % 10 == 0

    def login(self):
        customer = input("Enter your card number:")
        pin = input("Enter your PIN:")
        if self.db_check('number', customer):
            self.cursor.execute(f'SELECT * FROM card WHERE number = {customer}')
            card = self.cursor.fetchone()
            if int(pin) == int(card[2]):
                print("You have successfully logged in!")
                while True:
                    self.choice = int(input("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n"))
                    if self.choice == 0:
                        raise Exception("Bye!")
                    elif self.choice == 1:
                        self.cursor.execute(f"SELECT balance FROM card WHERE number = {customer}")
                        print(self.cursor.fetchone()[0])
                    elif self.choice == 2:
                        income = int(input("Enter income:\n"))
                        self.cursor.execute(f'UPDATE card SET balance = balance + {income} WHERE number = {customer}')
                        conn.commit()
                        print("Income was added!")
                    elif self.choice == 3:
                        receive = input("Enter card number:\n")
                        if self.luhn(receive):
                            if self.db_check('number', receive):
                                amount = int(input("Enter how much money you want to transfer:"))
                                self.cursor.execute(f'SELECT balance FROM card WHERE number = {customer}')
                                if amount <= self.cursor.fetchone()[0]:
                                    self.cursor.execute(f'UPDATE card SET balance = balance - {amount} WHERE number = {customer}')
                                    self.cursor.execute(f'UPDATE card SET balance = balance + {amount} WHERE number = {receive}')
                                    conn.commit()
                                    print("Success!")
                                else:
                                    print("Not enough money!")
                            else:
                                print("Such a card does not exist.")
                        else:
                            print("Probably you made mistake in the card number. Please try again!")
                    elif self.choice == 4:
                        self.cursor.execute(f'DELETE FROM card WHERE number = {customer}')
                        conn.commit()
                        print("The account has been closed!")
                        break
                    elif self.choice == 5:
                        print("You have successfully logged out!")
                        break
            else:
                print(pin, card[2])
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")

    def process(self):
        try:
            while True:
                self.choice = int(input("1. Create an account\n2. Log into account\n0. Exit\n"))
                if self.choice == 0:
                    raise Exception("Bye!")
                elif self.choice == 1:
                    self.create()
                elif self.choice == 2:
                    self.login()
                else:
                    print("Invalid option")
        except Exception as e:
            print(str(e))

bank = SimpleBank(conn)
bank.process()
