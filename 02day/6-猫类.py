class cat():
    def eat(self):
        print("猫吃猫粮")
    def introduce(self):
        print("我叫%s,今年%d岁,是%s的猫"%(self.name,self.age,self.color))




a = cat()
a.eat()
a.name = "波斯猫"
a.age = 16
a.color = "白色"
a.introduce()

b = cat()
b.eat()
b.name = "加菲猫"
b.age = 11
b.color = "黄色"
b.introduce()
