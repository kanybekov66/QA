class CoffeeMachine:
    def __init__(self):
        self.milk = 1000
        self.coffee = 1000
        self.sugar = 1000



    def __substract_milk(self, milk):
        self.milk -= milk


    def __substract_coffee(self, coffee):
        self.coffee -= coffee


    def __substract_sugar(self, sugar):
        self.sugar -= sugar


    def make_coffee(self, milk, coffee, sugar):

        if milk <= self.milk and coffee <= self.coffee and sugar <= self.sugar:
            self.__substract_milk(milk)
            self.__substract_coffee(coffee)
            self.__substract_sugar(sugar)
            print("Процесс приготовления кофе завершен!")
        else:
            print(f"Пополните запасы молока на {milk - self.milk} гр! Пополните запасы кофе на {coffee - self.coffee} мл! Пополните запасы сахара на {sugar - self.sugar} гр!")




if __name__=='__main__' :
    kahve = CoffeeMachine()
    print(kahve.milk, kahve.sugar, kahve.sugar)
    kahve.make_coffee(200, 200, 200)
    print(kahve.milk, kahve.sugar, kahve.sugar)
    kahve.make_coffee(1200, 1600, 1600)
