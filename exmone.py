import datetime
class Bank:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.history = []
        self.moves = 0


    def pluss(self):
        print ("выберите сумму пополнения ")
        abc = 0
        abc =int(input())

        self.balance += abc
        self.history.append({"пополнение баланса ", abc })
        print ("ваш баланс", self.balance , " \n")
    def minuss(self):
        print("выберите сумму вывода ")
        print("ваш баланс", self.balance)
        abc = int(input())
        if self.balance <= abc:
            print("ваш баланс", self.balance)
            print("не хватает средств \n ", " \n")
            self.history.append({"попытка вывода средств ", abc})

        else:
            self.balance -= abc
            self.history.append({"вывод средств ", abc})
            print("ваш баланс", self.balance)

    def historry(self):
        print ("ваша история : ")
        print(self.history)



    def balanceee(self):
        print("ваш баланс", self.balance)
        self.history.append("просмотр баланса ")


    # def choise(self,a):
    #         if qwe == 1:
    #             self.pluss()
    #         if qwe == 2:
    #             self.minuss()
    #         if qwe == 3:
    #             self.history()
    #         else:
    #             self.balance()
























