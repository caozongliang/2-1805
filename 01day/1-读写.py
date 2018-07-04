#创建文件,写入内容
import time
print("正在写入...")
f = open("1.txt","w")
f.write("啦啦啦,德玛西亚")
f.close
time.sleep(2)
print("写入成功")

time.sleep(3)
print("正在读取...")

#读取刚才的文件
f = open("1.txt","r")
a = f.read()
print(a)
f.close()

#创建新的备份文件,将刚才的读取到的内容写入新文件
time.sleep(3)
print("正在备份")
n = open("1back.txt","w")
n.write(a)
n.close()
time.sleep(3)
print("备份成功")
