name = input("请输入要备份的文件名字")
a = open(name,"r")
c = a.read()
position = name.rfind(".")
b = name[:position]+"back"+".txt"
f = open(b,"w")
f.write(c)
a.close()
f.close()
