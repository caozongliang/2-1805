#定义工具类
class tool():
    #具有添加十个数字的行为
    def add(self):
        import random
        list = []
        while len(list)<10:
            num = random.randint(1,100)
            if num in list:
                continue
            list.append(num)
        print(list)
#定义对象a
a=tool()
#调用行为
a.add()
            
