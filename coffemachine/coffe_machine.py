import random
text = ("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")

waters = random.randint(0, 1000)
milks = random.randint(0, 500)
beamss = random.randint(0, 250)
cupss = random.randint(0, 25)

cost_espresso = 4
cost_latte = 7
cost_cappuchino = 6

waterf = int(0)
milkf = int(0)
beamsf = int(0)
cupsf = int(0)
n = 0

def espresso(message_espresso):
    global water, milk, beams, cups, cost_espresso, waterf, milkf, beamsf, cupsf, n
    water = int((waters + waterf) / 250)
    beams = int((beamss + beamsf) / 16)
    cups = int(cupss + cupsf)
    minimum = min([water, beams, cups])
    cup = int(input("How many cups of coffe u need?"))
    final_cost = cup * cost_espresso
    if minimum >= cup:
        money = int(input(f"Please, insert cash - {final_cost}"))
        if money == final_cost:
            print(text)
            n = n + money
            coffemachine('')
        elif money < final_cost:
            print("You have insert not enough amount of money")
            espresso('espresso')
        else:
            change = money - final_cost
            print("Take ur change")
            print(text)
    elif (minimum < cup):
        print("We have not enough ingredients, sorry")
        print("pls, fill machine")
        coffemachine('')


def latte(message_latte):
    global water, milk, beams, cups, cost_latte, waterf, milkf, beamsf, cupsf, n
    water =  int((waters + waterf) / 350)
    milk = int((milks + milkf) / 75)
    beams = int((beamss - beamsf) / 20)
    cups = int(cupss + cupsf)
    minimum = min([water, milk, beams, cups])
    cup = int(input("How many cups of coffe u need?"))
    final_cost = cup * cost_latte
    if (minimum >= cup):
        money = int(input(f"Please, insert cash - {final_cost}"))
        if money == final_cost:
            print(text)
            n = n + money
        elif money < final_cost:
            print("You have insert not enough amount of money")
            latte('latte')
        else:
            change = money - final_cost
            print(f"Take ur change {change}")
            print(text)
    elif (minimum < cup):
        print("We have not enough ingredients, sorry")
        print("pls, fill machine")
        coffemachine('')


def cappuchino(message_latte):
    global water, milk, beams, cups, cost_cappuchino, waterf, milkf, beamsf, cupsf, n
    water = int((waters + waterf) / 200)
    milk = int((milks + milkf) / 100)
    beams = int((beamss - beamsf) / 12)
    cups = int(cupss + cupsf)
    minimum = min([water, milk, beams, cups])
    cup = int(input("How many cups of coffe u need?"))
    final_cost = cup * cost_cappuchino

    if (minimum >= cup):
        money = int(input(f"Please, insert cash - {final_cost}"))
        if money == final_cost:
            print(text)
            n = n + money
        elif money < final_cost:
            print("You have insert not enough amount of money")
            cappuchino('cappuchino')
        else:
            change = money - final_cost
            print(f"Take ur change {change}")
            print(text)
    elif (minimum < cup):
        print("We have not enough ingredients, sorry")
        print("pls, fill machine")
        coffemachine('')

def take():
    global n
    print(f"{n} money")
    n = 0
    coffemachine('')


def coffemachine(message_coffemachine):
    global waters, waterf, milks, milkf, beamss, beamsf, cupss, cupsf, cost_latte, cost_espresso, cost_cappuchino, n
    print("""What u whant to do?: 
    1 - buy, 
    2 - fill, 
    3 - take, 
    4 - show amount of ingredients""")
    answer = int(input())
    if answer == 1:
        print("""What coffee do u want?
        1 - espresso
        2 - latte
        3 - cappuccino""")
        choose_coffee = int(input())
        if choose_coffee == 1:
            espresso('')
        elif choose_coffee == 2:
            latte('')
        elif choose_coffee == 3:
            cappuchino('')
    elif answer == 2:
        waterf = int(input("insert amount of added water"))
        milkf = int(input("insert amount of added milk"))
        beamsf = int(input("insert amount of added beams"))
        cupsf = int(input("insert amount of added cups"))
    elif answer == 3:
        take()

    elif answer == 4:
        print(waters + waterf)
        print(milks + milkf)
        print(beamss + beamsf)
        print(cupss + cupsf)
        print(n)
    coffemachine('')


coffemachine('')
# сделай 4 коммит, это все 4 коммит, 5 в будущем
