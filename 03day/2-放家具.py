class home():
    def __init__(self,address,area):
        self.address = address
        self.area = area
    def __str__(self):
        msg = "我的家在%s,面积是%s"%(address,area)
        return msg
    def addjiaju(self):
        self.jiaju.append(bed)
class bed():
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "有%s%s"%(name,area)
laowang = home()
laowang.address = "北京长安大街"
laowang.area = "一万三"
laowang.addjiaju()
c = bed()
c.name = "席梦思大床"
c.area = "老大了"

