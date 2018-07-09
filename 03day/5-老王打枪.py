class person():
    def __init__(self,name):
        self.name = name
        self.xue = 100

    def naqiang(self,gun):
        self.gun = gun


    def zhuangzidan(self,danjia,aidan):
        danjia.list.append(zidan)

    def zhuangdanjia(self,gun,danjia):
        gun.danjia = danjia

    def opengun(delf,diren):
        zidan = self.gun.danjia.tanzidan()
        zidan.kill(diren)
    def diaoxue(self,count):
        self.xue-= count
        print("还剩多少%d"%self.xue)
        if self.xue <= 0:
            print("挂了")
class gun():
    def __init__(self,name):
        self.name = name
        self.danjia = None

class danjia():
    def __init__(self,name,cuout):
        self.name = name
        self.count = count
        self.list = []
    def tanzidan(self):
        zidan = self.list.pop()
        return zidan
class zidan():
    def __init__(self,name,kill_count):
        self.name = name
        self.kill_count = kill_count

    def kill(self,diren):
        diren.diaoxue(self.kill_count)

laowang = person("老王")
ak47 = gun
danjia = danjia("快速扩容",40)

laowang.naqiang(gun)
for i in range(40):
    zidan = zidan()
    laowang.zhuangzidan(danjia,zidan)

laowang.zhuangzidan(ak47,danjia)
laosong = person("老宋")

laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)

        
























