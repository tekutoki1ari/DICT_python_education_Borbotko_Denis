import random


class DinnerParty:
    def __init__(self, friends, money):
        self.friends = friends
        self.money = money

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
                print('no one going to be lucky:>>> ')
                cash = int(input("enter amount of money:>>> "))
                amount = cash / invite_list_amount
                sum_true = round(amount, 2)
                for i in range(invite_list_amount):
                    self.money.append(sum_true)
                print(dict(zip(self.friends[:invite_list_amount], self.money)))
            else:
                lucky = random.choice(self.friends)
                print(f'the {lucky} is lucky')


dinner_party = DinnerParty([], [])
dinner_party.invite()
