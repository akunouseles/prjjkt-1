#print ("hellow world")
class Que:
    # print ("what")
    col=0
    def __init__(self, height=160,age = 13, name=None):
        self.height=height
        #print(self)
        print("я негар неграм быть сложна но я негар")
        Que.col+=1
        self.name=name
        self.age=age
    def grow(self,height=5):
        self.height+=height
    def __str__(self):
        return f"Mine name is  {self.name}"

student1=Que()
student1=Que(age=15)
student1=Que(name="Anton")
print(student1.__str__())
print (student1.name)
print( "возраст", student1.age, student1.name,"average height ", student1.height)
student2=Que(height=10000)
print("fsdfsdfwefwe", student2.height)
print(student1.col)
print("papagagemabodi")
print(student2.col)
student1.grow(height=5)
print(student1.height)
student2.grow(height=2^15)
print(student2.height)














