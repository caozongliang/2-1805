class Home():
    def __init__(self,address,price,area):
        self.address = address
        self.price = price
        self.area = area
        self.list = []
    def __str__(self):
        msg = "家的地址是%s价格是%d万面积是%d"%(self.address,self.price,self.area)
        return msg
    def move(self,bed):
        import time
        i = 0
        while True:
            if self.area<bed.area:
                print("满了,装不下了")
                print("共装了%d张床"%i)
                break
            else:                    
                self.list.append(bed)
                self.area = self.area-bed.area
                time.sleep(1)
                print("装了一张床,剩余面积%d"%self.area)
                i+=1

class bed():
    def __init__(self,area):
        self.area = area
    def __str__(self):
        msg = "床的面积是%d"%self.area
        return msg









laowang = Home("北京",1500,120)
print(laowang)
c = bed(8)
print(c)
laowang.move(c)



