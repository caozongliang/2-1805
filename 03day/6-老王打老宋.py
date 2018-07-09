import time
class people():
    def __init__(self,name):
        self.name = name
        self.hp = 100
        
    def __str__(self):
        return "%s在决赛圈遇到了敌人..."%(self.name)

    def Naqiang(self,qiang):
        self.qiang = qiang
        print("%s掏出了自己的%s"%(self.name,self.qiang))
        

    def dadada(self,diren):
        self.diren = diren
        print("啪...")
        i = 0
        while True:
            time.sleep(1)
            print("%s一枪命中敌人头部,掉血%d,剩余子弹%d"%(self.name,80,5-i))
            i+=1
            self.hp-=80
            if self.hp <0:
                print("敌人挂了")
                break

class qiang():
    def __init__(self,name):
        self.name = name
        self.count = 0
        
    def add(self):
        print("%s正在装弹.."%self.name)      
        for i in range(5):
            time.sleep(1)
            print("咔...")
            self.count+=1
        print("当前子弹:%d"%self.count)



laowang = people("老王")
laosong = people("老宋")
q = qiang("98k")
print(laowang)
laowang.Naqiang("98k")
q.add()
laowang.dadada(laosong)

