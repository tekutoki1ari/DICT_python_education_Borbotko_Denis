import random


class DinnerParty:
    def __init__(self, friends, money, lucky):
        self.friends = friends
        self.money = money
        self.lucky = lucky

    def invite(self):
        self.friends = ['Denis', 'Marlen', 'Bogdan', 'Stanislaw']
        invite_list_amount = int(input('enter the amount of people who want to join:>>> '))
        print(self.friends[:invite_list_amount])
        if invite_list_amount <= 0:
            print('No one is joining for the party')
        elif invite_list_amount > 0:
            select = int(input('''do u want to choose a lucky one?
                            1 - no
                            2 - yes
                            '''))
            if select == 1:
                print('no one going to be lucky')
                cash = int(input("enter amount of money:>>> "))
                amount = cash / invite_list_amount
                sum_true = round(amount, 2)
                for i in range(invite_list_amount):
                    self.money.append(sum_true)
                print(dict(zip(self.friends[:invite_list_amount], self.money)))
            else:
                lucky = random.choice(self.friends[:invite_list_amount])
                print(lucky)
                cash = int(input("enter amount of money:>>> "))
                amount = cash / (invite_list_amount - 1)
                sum_true = round(amount, 2)
                clever = self.friends.index(lucky)
                for i in range(invite_list_amount):
                    if i == clever:
                        self.money.append(0)
                    else:
                        self.money.append(sum_true)
                print(dict(zip(self.friends[:invite_list_amount], self.money)))


dinner_party = DinnerParty([], [], 'default')
dinner_party.invite()
