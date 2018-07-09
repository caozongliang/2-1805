class people():
    def __init__(self,name,xue,dan):
        self.name = name
        self.xue = xue
        self.dan = dan 
    def __str__(self):                
        return "%s血量为%d"%(self.name,self.xue)
    def naqiang(self,qiang_name,dan):
        print("拿到一把%s,子弹为%d"%(self.qiang_name,self.dan))
    def addzidan(self,name):
        self.dan=self.dan+10
        print("装%s子弹%d发"%(self.name,self.dan))
class qiang():
    def __init__(self,qiang_name,ad):
        self.qiang_name = qiang_name
        self.ad = ad
    def __str__(self):
        pass
    def seji(self):
        print("哒哒哒...")
class zidan():
    def __init__(self,name):
        self.name = name





laowang = people("老王",100,0)
print(laowang)
AK = qiang("98K",80)
a = zidan("7.62")
laowang.naqiang("98K",80)
laowang.addzidan("7.62")
laowang.siji()
