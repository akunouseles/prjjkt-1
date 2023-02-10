# #print ("hellow world")
# class Que:
#    col=0
#    def __init__(self, height=160,age = 13, name=None):
#       self.height=height
#        #print(self)
#        print("я негар неграм быть сложна но я негар")
#        Que.col+=1
#        self.name=name
#       self.age=age
#   def grow(self,height=5):
#        self.height+=height
#    def __str__(self):
#       return f"Mine name is  {self.name}"
#
# student1=Que()
# student1=Que(age=15)
# student1=Que(name="Anton")
# print(student1.__str__())
# print (student1.name)
# print( "возраст", student1.age, student1.name,"average height ", student1.height)
# student2=Que(height=10000)
# print("fsdfsdfwefwe", student2.height)
# print(student1.col)
# print("papagagemabodi")
# print(student2.col)
# student1.grow(height=5)
# print(student1.height)
# student2.grow(height=2^15)
# print(student2.height)
from random import randint
class Simualator:
    def __init__(self, name):
        self.name=name
        self.happyness= 50
        self.progress = 0
        self.opportunity2live = 50
        self.ifalive = True
        self.money = 100
    def study(self):
        print ("Время учиться")
        self.happyness -=20
        self.progress += 1.5
        self.opportunity2live -= 20
        self.money -= 20
    def sleep(self):
        self.happyness += 1
        self.progress -=0.2
        self.opportunity2live +=5

    def rest(self):
        self.happyness += 5
        self.progress -= 1
        self.opportunity2live += 5
        self.money -=40

    def ifaliveee(self):
        if self.progress <= 0:
            self.study()
        if self.money <= 0:
            self.work()
            exit()

    def day(self):

        print("uroven' schast'a", self.happyness)
        print("uroven' progressa", self.progress)
        print("uroven' zuzni", self.opportunity2live)
        print("ziv?", self.ifalive)
        print("denngi", self.money)
        print("=======================================")

    def choice(self , numDay):
        print("==================================================")
        numDay = "День # "+str(numDay)+" из жизни студента " + self.name
        print(numDay)
        rnd=randint(1,4)
        if rnd==1: self.study()
        elif rnd==2: self.sleep()
        elif rnd==3: self.rest()
        else: self.work()
        self.ifaliveee()
        self.day()

    def work(self):
        self.progress -= 2
        self.money += 100
        self.opportunity2live -=10


studenFirst = Simualator(name="Субота")
for i in range (1,366):
    studenFirst.choice(i)


class Dog:
    def __init__(self, name):
        self.name=name
        self.happyness= 50
        self.hungry = 0
        self.energy = 100
        self.smartness = 0
        self.boredom = 50


    def walk(self):
        self.happyness +=20
        self.hungry +=20
        self.energy -=20
        self.smartness -=10
        self.boredom -= 15

    def eating(self):
        self.happyness += 5
        self.hungry -= 35
        self.energy += 10
        self.smartness -= 5
        self.boredom +=5

    def studyy(self):
        self.happyness -= 20
        self.hungry +=40
        self.energy -=35
        self.smartness += 25
        self.boredom += 25

    def sleepp(self):
        self.happyness += 10
        self.hungry += 35
        self.energy = 100
        self.smartness -= 5
        self.boredom += 5

    def playing(self):
        self.happyness -= 20
        self.hungry += 40
        self.energy -= 35
        self.smartness += 25
        self.boredom -= 25

    def hour(self):
        print("uroven' schast'a", self.happyness)
        print("uroven' yma", self.smartness)
        print("uroven' skyki", self.boredom)
        print("uroven energii", self.energy)
        print("uroven goloda", self.hungry)
        print("=======================================")

    def choicee(self , numDay):
        print("==================================================")
        numDay = "Час # "+str(numDay)+"из жизни студента " + self.name
        print(numDay)
        rnd=randint(1,5)
        if rnd==1: self.studyy()
        elif rnd==2: self.sleepp()
        elif rnd==3: self.walk()
        elif rnd == 4: self.eating()
        else: self.playing()
        self.hour()

doggy = Dog(name = "Sharik")
for i in range (1,13):
    doggy.choicee(i)

















