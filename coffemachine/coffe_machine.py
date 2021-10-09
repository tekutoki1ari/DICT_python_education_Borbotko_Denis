import random

print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")
# water = int(random.randint(0, 1000))
# milk = int(random.randint(0, 1000))
# zerna = int(random.randint(0, 1000))
water_cup = 200
milk_cup = 50
zerna_cup = 15
want_coffee = int(input("vvedite colwo chashek: "))
print("For ", want_coffee,  " cups you will need")
print(str(water_cup * want_coffee))
print(str(milk_cup * want_coffee))
print(str(zerna_cup * want_coffee))