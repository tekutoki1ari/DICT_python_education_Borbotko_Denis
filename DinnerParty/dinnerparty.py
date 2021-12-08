# import random


class DinnerParty:
    def __init__(self, friends, money):
        self.friends = friends
        self.money = money

    def invite(self):
        self.friends = ['Denis', 'Marlen', 'Bogdan', 'Stanislaw']
        invite_list_amount = int(input('enter the amount of people who want to join:>>> '))
        print(self.friends[:invite_list_amount])
        if invite_list_amount == 0:
            print('No one is joining for the party')
        else:
            cash = int(input("enter amount of money"))
            summ = cash / invite_list_amount
            summ_true = round(summ, 2)
            for i in range(invite_list_amount):
                self.money.append(summ_true)
            print(dict(zip(self.friends[:invite_list_amount], self.money)))


dinner_party = DinnerParty([], [])
dinner_party.invite()
