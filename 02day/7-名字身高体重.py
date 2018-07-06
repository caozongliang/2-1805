class people():
    def __init__(self,name,height,weight,age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
    def introduce(self):
        print("我的名字是%s,身高%d,体重%d,年龄%d"%(self.name,self.height,self.weight,self.age))        
cc = people('cc',180,120,18)
cc.introduce()
        
        














