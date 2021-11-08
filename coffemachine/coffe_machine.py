import random
text = ("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")

waters = 0
milks = 0
beamss = 0
cupss = 0
cost = 0

# cost_espresso = 4
# cost_latte = 7
# cost_cappuchino = 6
#
# waterf = int(0)
# milkf = int(0)
# beamsf = int(0)
# cupsf = int(0)
# n = 0

save = open("save.txt", "r")
line = save.readlines()
try:
    if int(line[0]) == 0 and int(line[1]) == 0 and int(line[2]) == 0 and int(line[3]) == 0 and int(line[4]) == 0:
        save.close()
        waters = random.randint(0, 10000)
        milks = random.randint(0, 5000)
        beamss = random.randint(0, 1500)
        cupss = random.randint(0, 50)
        cost = 0
        save = open('save.txt', 'w')
        save.write(str(waters) + f"\n")
        save.write(str(milks) + f"\n")
        save.write(str(beamss) + f"\n")
        save.write(str(cupss) + f"\n")
        save.write(str(cost) + f"\n")
        save.close()
    else:
        save = open("save.txt")
        waters = int(line[0])
        milks = int(line[1])
        beamss = int(line[2])
        cups = int(line[3])
        cost = int(line[4])
        save.close()
finally:
    pass


class Coffeemachine:
    def __init__(self, buy, fill, take, remaining, exit):
        self.buy = buy
        self.fill = fill
        self.take = take
        self.remaining = remaining
        self.exit = exit


function = Coffeemachine("buy", "fill", "take", "remaining", "exit")


def Function():
    global save
    choose = input(str("Chose function: buy, fill, take, remaining or exit"))
    if choose == function.buy:
        Buy()
    elif choose == function.take:
        take()
    elif choose == function.remaining:
        remaining()
    elif choose == function.exit:
        save = open("save.txt", "w")
        save.write(f"{str(waters)}\n")
        save.write(f"{str(milks)}\n")
        save.write(f"{str(cupss)}\n")
        save.write(f"{str(cost)}\n")
        save.close()
        print("good bye")
    else:
        print("try again")
        Function()


def Buy():
    global cost
    choose = int(input("chose function: 1-espresso, 2-lqtte, 3-cappuccino, 4-back"))
    if choose == 1:
        espresso()
    elif choose == 2:
        latte()
    elif choose == 3:
        cappuccino()
    elif choose == 4:
        Function()
    else:
        print("try again")


def espresso():
    global cost, waters, beamss, cupss, save, cost
    cost = 4
    water = int(waters / 250)
    beams = int(beamss / 16)
    minimum = min([water])
    cups_need = int(input("how many cups of coffee do u need?"))
    n = cost * cups_need
    if minimum >= cups_need:
        give_money = int(input(f"insert {n} money"))
        if give_money >= n:
            change = give_money - n
            print(f"Your change {change}")
            waters = water * 250 * cups_need
            beamss = beams * 16 * cups_need
            cupss = cupss - cups_need
            cost = cost + n
            print(text)
            Function()
        else:
            print("you have insert not enough money")
            espresso()

    elif minimum < cups_need:
        if cups_need > water:
            enough_water = (cups_need * 250) - waters
            print(f"for {cups_need} cups of coffe you dont have enough {enough_water} ml of water")
            Fill()
        elif cups_need > beams:
            enough_beams = (cups_need * 16) - beamss
            print(f"for {cups_need} cups of coffe you dont have enough {enough_beams} g of beams")
            Fill()
        elif cups_need > cupss:
            enough_cups = cups_need - cupss
            print(f"for {cups_need} cups of coffe you dont have enough {enough_cups} cups")
            Fill()


def latte():
    global cost, waters, milks, beamss, cupss, save, cost
    cost = 7
    water = int(waters / 350)
    milk = int(milks / 75)
    beams = int(beamss / 20)
    minimum = min([water, milk, beams, cups])
    cups_need = int(input("how many cups of coffee do u need?"))
    n = cost * cups_need
    if minimum >= cups_need:
        give_money = int(input(f"insert {n} money"))
        if give_money >= n:
            change = give_money - n
            print(f"your change {change}")
            waters = waters - 350 * cups_need
            milks = milks - 75 * cups_need
            beamss = beamss - 20 * cups_need
            cupss = cups - cups_need
            cost = cost + n
            print(text)
            Function()
        else:
            print("you have insert not enough money")
        latte()
    elif minimum < cups_need:
        if cups_need > water:
            enough_water = (cups_need * 350) - waters
            print(f"for {cups_need} cups of coffee we dont have enough {enough_water} ml of water")
            Fill()
        elif cups_need > milk:
            enough_milk = (cups_need * 75) - milks
            print(f"for {cups_need} cups of coffee we dont have enough {enough_milk} ml of milk")
            Fill()
        elif cups_need > beams:
            enough_beams = (cups_need * 20) - cupss
            print(f"for {cups_need} cups of coffee we dont have enough {enough_beams} g of beams")
            Fill()
        elif cups_need > cupss:
            enough_cups = cups_need - cupss
            print(f"for {cups_need} cups of coffee we dont have enough {enough_cups} cups")
            Fill()


def cappuccino():
    global cost, waters, milks, beamss, cupss, money
    cost = 6
    water = int(waters / 200)
    milk = int(milks / 100)
    beams = int(beamss / 12)
    minimum = min([water, milk, beams, cups])
    cups_need = int(input("How many cups of coffee do u need?"))
    n = cost * cups_need
    if minimum >= cups_need:
        give_money = int(input(f"insert {n} money"))
        if give_money >= n:
            change = give_money - n
            print(f"your change {change}")
            waters = waters - 200 * cups_need
            milks = milks - 100 * cups_need
            beamss = beamss - 12 * cups_need
            cost = cost + change
            print(text)
            Function()
        else:
            print("You have insert not enough money")
            cappuccino()
    elif minimum < cups_need:
        if cups_need > water:
            enough_water = (cups_need * 200) - waters
            print(f"for {cups_need} cups of coffee we dont have enough {enough_water} ml of water")
            Fill()
        elif cups_need > milk:
            enough_milk = (cups_need * 100) - milks
            print(f"for {cups_need} cups of coffee we dont have enough {enough_milk} ml of milk")
            Fill()
        elif cups_need > beamss:
            enough_beams = (cups_need * 12) - beamss
            print(f"for {cups_need} cups of coffee we dont have enough {enough_beams} g of beams")
            Fill()
        elif cups_need > cups:
            enough_cups = cups_need - cupss
            print(f"for {cups_need} cups of coffee we dont have enough {enough_cups} cups")
            Fill()


def Fill():
    global save, waters, milks, cupss, beamss
    fill = int(input("what u want to add? 1 - water, 2 - milk, 3 - beams, 4 - cups, 5 - back"))
    if fill == 1:
        water_add = int(input("How many water do u want to add?"))
        waters = waters + water_add
        Function()
    elif fill == 2:
        milk_add = int(input("How many milk do u want to add?"))
        milks = milks + milk_add
        Function()
    elif fill == 3:
        beams_add = int(input("How many beams do u want to add?"))
        beamss = beamss + beams_add
    elif fill == 4:
        cups_add = int(input("How many cups do u want to add?"))
        cupss = cupss + cups_add
        Function()
    elif fill == 5:
        Function()
    else:
        print("Unknown command")
        Fill()


def take():
    global cost
    print(cost)
    take_money = int(input("how many money do u want to take away?"))
    cost = cost - take_money
    Function()


def remaining():
    print(f"water - {waters}, milk - {milks}, beams - {beamss}, cups - {cupss}, money - {cost}")
    Function()


Function()
