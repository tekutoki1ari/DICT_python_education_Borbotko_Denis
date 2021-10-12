print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")

water_cup = int(input("Write how many ml of water the coffee machine has: "))
milk_cup = int(input("Write how many ml of milk the coffee machine has: "))
beams_cup = int(input("Write how many grams of coffee beans the coffee machine has: "))
want_coffee = int(input("vvedite colwo chashek: "))

one_cup_w = (water_cup / 250)
one_cup_m = (milk_cup / 50)
one_cup_b = (beams_cup / 15)
one_cup_minimum = min(one_cup_w, one_cup_m, one_cup_b)
one_cup_N = int(one_cup_minimum - want_coffee)
one_cup_Nmin1 = int(want_coffee - one_cup_minimum)

if one_cup_minimum >= want_coffee:
    print("Yes, I can make that amount of coffee and " + str(one_cup_N) + " even more")
elif one_cup_minimum < want_coffee:
    print("No, I can make only " + str(one_cup_Nmin1) + " cups of coffee")
