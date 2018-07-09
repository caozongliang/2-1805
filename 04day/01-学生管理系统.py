import os
class people():
    
    def __init__(self,name):
        self.name = name
        
        
    def add(self,name):
        self.xh = input("输入学号")
        f = open(name+".txt","w")        
        f.write("名字:%s\t学号%s\t"%(self.name,self.xh))
        f.close
    def dele(self,name):
        os.remove(name+".txt")

    def cat(self):
        a = input("输入名字")
        f = open(a+'.txt','r')
        b = f.read()
        print(b)
        f.close

class fun():
    def __str__(self):
        return "1.添加  2.删除  3.修改  4.查看"
    def choose(self):
        a = input("请选择功能序号")
        if a == '1':
            return 1
        elif a == '2':
            return 2
        elif a == '4':
            return 4
while True:            
    cc = fun()
    print(cc)
    if cc.choose() == 1:
        name = input("输入名字")
        laowang = people(name)
        laowang.add(name)
    elif cc.choose() == 2:
        name = input("输入姓名")
        laowang = people(name)
        laowang.dele(name)
    elif cc.choose() == 4:
        laowang.cat()




