def making():
    print("Starting to make a coffee")
    print("Grinding coffee beans")
    print("Boiling water")
    print("Mixing boiled water with crushed coffee beans")
    print("Pouring coffee into the cup")
    print("Pouring some milk into the cup")
    print("Coffee is ready!")

def ingredients():
    cups = int(input("How many cups of coffee will you need?"))
    print("For ", cups, " cups of coffee you will need:")
    print(cups * 200, " ml of water")
    print(cups * 50," ml of milk")
    print(cups * 15, " g of coffee beans")

def available():
    water = int(input("Write how many ml of water the coffee machine has:"))
    milk = int(input("Write how many ml of milk the coffee machine has:"))
    coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
    cups = int(input("Write how many cups of coffee you will need:"))
    max_cups = min(water // 200, milk // 50, beans // 15)
    if max_cups < cups:
        print("No, I can only make " + str(max_cups) + " cups of coffee")
    else:
        print("Yes, I can make that amount of coffee" + ("" if max_cups == cups else " (and even " + str(max_cups - cups) + " more than that)"))

def buy(money, water, milk, coffee, cups):
    selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - main menu:")
    if selection == "1":
        if water - 250 < 0:
            print("Sorry, not enough water!")
        elif coffee - 16 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            money += 4
            water -= 250
            coffee -= 16
            cups -= 1
    elif selection == "2":
        if water - 350 < 0:
            print("Sorry, not enough water!")
        elif milk - 75 < 0:
            print("Sorry, not enough milk!")
        elif coffee - 20 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            money += 7
            water -= 350
            milk -= 75
            coffee -= 20
            cups -= 1
    elif selection == "3":
        if water - 200 < 0:
            print("Sorry, not enough water!")
        elif milk - 100 < 0:
            print("Sorry, not enough milk!")
        elif coffee - 12 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            money += 6
            water -= 200
            milk -= 100
            coffee -= 12
            cups -= 1
    else:
        pass
    return money, water, milk, coffee, cups

def fill(water, milk, coffee, cups):
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    coffee += int(input("Write how many grams of coffee beans do you want to add:"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:"))
    return water, milk, coffee, cups

def take(money):
    print("I gave you $", money)
    return 0

def display(money, water, milk, coffee, cups):
    print("The coffee machine has:")
    print(water, " of water")
    print(milk," of milk")
    print(coffee," of coffee beans")
    print(cups," of disposable cups")
    print(money," of money")

def process(money, water, milk, coffee, cups, choice):
    choice = input("Write action (buy, fill, take, remaining, exit):")
    if choice == "buy":
        money, water, milk, coffee, cups = buy(money, water, milk, coffee, cups)
    elif choice == "fill":
        water, milk, coffee, cups = fill(water, milk, coffee, cups)
    elif choice == "take":
        money = take(money)
    elif choice == "remaining":
        display(money, water, milk, coffee, cups)
    else:
        pass
    return money, water, milk, coffee, cups, choice


#starting amounts
money, water, milk, coffee, cups, choice = 550, 400, 540, 120, 9, ""

while choice != "exit":
    if choice == "exit":
        break
    money, water, milk, coffee, cups, choice = process(money, water, milk, coffee, cups, choice)
