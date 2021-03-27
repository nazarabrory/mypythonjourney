class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

        self.action = None

    actions = ['buy', 'fill', 'take', 'remaining', 'exit']

    def change_action(self, do):
        if self.action is None:
            if do in self.actions:
                self.action = do
            else:
                return f'Invalid input, please select one of this modes {self.actions}:'

        if self.action == "buy":  # buy
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            coffee_selection = input()
            if coffee_selection == "1":
                return self.buy_espresso()
            elif coffee_selection == "2":
                return self.buy_latte()
            elif coffee_selection == "3":
                return self.buy_cappucino()
            elif coffee_selection == "back":
                return "\n" + self.welcome_screen()
        elif self.action == "fill":  # fill
            print('Write how many ml of water do you want to add:')
            water_add = int(input())
            self.water += water_add
            print('Write how many ml of milk do you want to add: ')
            milk_add = int(input())
            self.milk += milk_add
            print('Write how many grams coffee beans do you want to add:')
            beans_add = int(input())
            self.beans += beans_add
            print('Write how many disposable cups of coffee do you want to add:')
            cups_add = int(input())
            self.cups += cups_add
            return "\n" + self.welcome_screen()
        elif self.action == "take":  # take
            money_taken = self.money
            self.money = 0
            return f'I gave you {money_taken}' + '\n\n' + self.welcome_screen()
        elif self.action == "remaining":  # remaining
            return self.__str__() + "\n\n" + self.welcome_screen()
        elif self.action == "exit":  # exit
            return "Exiting."

    def buy_espresso(self):
        espresso_need = [250, 0, 16, 1, 4]  # [mater, milk, beans, cups, cost]
        can_make_espresso = True
        # checking wether resources is enough. If Yes, return "not enough" message. If No, proceed buy method.
        if self.water < espresso_need[0]:
            print(self.not_enough("water"))
            can_make_espresso = False
        if self.beans < espresso_need[2]:
            print(self.not_enough("beans"))
            can_make_espresso = False
        if self.cups < espresso_need[3]:
            print(self.not_enough("cups"))
            can_make_espresso = False
        if can_make_espresso:
            self.water -= espresso_need[0]
            self.beans -= espresso_need[3]
            self.money += espresso_need[4]
            print('I have enough resources, making you a coffee!')

        return "\n" + self.welcome_screen()

    def buy_latte(self):
        latte_need = [350, 75, 20, 1, 7]  # [water, milk, beans, cups, cost]
        can_make_latte = True
        # checking wether resources is enough. If Yes, return "not enough" message. If No, proceed buy method.
        if self.water < latte_need[0]:
            print(self.not_enough("water"))
            can_make_latte = False
        if self.milk < latte_need[1]:
            print(self.not_enough("milk"))
            can_make_latte = False
        if self.beans < latte_need[2]:
            print(self.not_enough("beans"))
            can_make_latte = False
        if self.cups < latte_need[3]:
            print(self.not_enough("cups"))
            can_make_latte = False
        if can_make_latte:
            self.water -= latte_need[0]
            self.milk -= latte_need[1]
            self.beans -= latte_need[2]
            self.cups -= latte_need[3]
            self.money += latte_need[4]
            print('I have enough resources, making you a coffee!')

        return "\n" + self.welcome_screen()

    def buy_cappucino(self):
        cappucino_need = [200, 100, 12, 1, 6]  # [water, milk, beans, cups, cost]
        can_make_cappucino = True
        # checking wether resources is enough. If Yes, return "not enough" message. If No, proceed buy method.
        if self.water < cappucino_need[0]:
            print(self.not_enough("water"))
            can_make_cappucino = False
        if self.milk < cappucino_need[1]:
            print(self.not_enough("milk"))
            can_make_cappucino = False
        if self.beans < cappucino_need[2]:
            print(self.not_enough("beans"))
            can_make_cappucino = False
        if self.cups < cappucino_need[3]:
            print(self.not_enough("cups"))
            can_make_cappucino = False
        if can_make_cappucino:
            self.water -= cappucino_need[0]
            self.milk -= cappucino_need[1]
            self.beans -= cappucino_need[2]
            self.cups -= cappucino_need[3]
            self.money += cappucino_need[4]
            print('I have enough resources, making you a coffee!')
        return "\n" + self.welcome_screen()

    @staticmethod
    def not_enough(resource):
        return f'Sorry, not enough {str(resource)}.'

    def welcome_screen(self):
        self.action = None
        return 'Write action (buy, fill, take, remaining, exit):'

    def __str__(self):
        return f"""This coffee machine has:
{self.water} ml of water.
{self.milk} ml of milk.
{self.beans} g of coffee beans.
{self.cups} of disposable cups.
{self.money} $ of money."""


coffee_maker = CoffeeMachine(0, 0, 0, 0, 0)
print(coffee_maker.welcome_screen())
while coffee_maker.action != "exit":
    print(coffee_maker.change_action(input()))
