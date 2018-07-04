import os
file = input("输入要批量重命名的文件夹")
a = os.listdir(file)
os.chdir(file)
for i in a:
    position = i.rfind(".")
    new_name = i[:position]+"精品"+i[position:]
    os.rename(i,new_name)    
