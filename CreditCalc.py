from math import ceil
from math import log

class CreditCalc:
    
    def __init__(self):
        principal = ""
        payment = ""
        interest = ""
        periods = ""
        choice = ""

    def months(self):
        self.principal = int(input("Enter credit principal:"))
        self.payment = float(input("Enter monthly payment:"))
        self.interest = float(input("Enter credit interest:")) / 1200
        self.periods = ceil(log(self.payment / (self.payment - self.interest * self.principal), 1 + self.interest))
        months = self.periods % 12
        years = self.periods // 12
        if months == 0:
            print(f"You need {years} years to repay this credit!" if years > 1 else f"You need {years} year to repay this credit!")
        elif years == 0:
            print(f"You need {months} months to repay this credit!")
        else:
            print(f"You need {years} years and {months} months to repay this credit!" if years > 1 else f"You need {years} year and {months} months to repay this credit!")
    
    def annuity(self):
        self.principal = int(input("Enter credit principal:")) 
        self.periods = int(input("Enter count of periods:"))
        self.interest = float(input("Enter credit interest:")) / 1200
        print(f"Your annuity payment = {ceil(self.principal * (self.interest * (1 + self.interest) ** self.periods) / ((1 + self.interest) ** self.periods - 1))}!")
    
    def principal(self):
        self.payment = float(input("Enter monthly payment:"))
        self.periods = int(input("Enter count of periods:"))
        self.interest = float(input("Enter credit interest:")) / 1200
        print(f"Your credit principal = {ceil(self.payment / ((self.interest * (1 + self.interest) ** self.periods) / ((1 + self.interest) ** self.periods - 1)))}!")
    
    def start(self):
        self.choice = input("""What do you want to calculate? 
        type "n" - for count of months,
        type "a" for annuity monthly payment, 
        type "p" - for credit principal:""")
        if self.choice == "n":
            self.months()
        elif self.choice == "a":
            self.annuity()
        elif self.choice == "p":
            self.principal()
            
credit_calculator = CreditCalc()
credit_calculator.start()