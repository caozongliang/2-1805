
#读取文件函数
def read_file(file):
    f = open(file,"r")
    content = f.read()
    print(content)
    f.close()
#文件写入内容函数
def write_file():
    old_file = input("输入要修改的文件")
    new_file = input("输入要写入的内容")
    f = open(old_file,"w")
    f.write(new_file)
    f.close()
    print("写入成功")

#文件备份函数
def backups(file1,file2):
    f = open(file1,"r")
    content = f.read()
    t = open(file2,"w")
    t.write(content)
    f.close()
    t.close()
    print("备份成功")
#文件批量重命名函数
def rename(folder):
    import os
    list = os.listdir(folder)
    os.chdir(folder)
    for i in list:
        position = i.rfind(".")
        os.rename(i,i[:position]+'专属'+i[position:])

while True:
    print("1.读取文件\t\t2.写入文件内容")
    print("3.备份文件\t\t4.文件批量重命名")
    print("\t\t0.退出")
    print("*"*50)
    fun = input("请选择功能")
    #读文件
    if fun == '1':
        file = input("输入要读取的文件名字")
        read_file(file)
    
    #写入文件
    elif fun == '2':
        write_file()

    #备份文件
    elif fun == '3':
        file1 = input("输入要备份的文件名字")
        file2 = input("请为备份后的新文件命名")
        backups(file1,file2)
    
    #重命名
    elif fun == '4':
        folder = input('我是傻子我怕谁:')
        rename(folder)
    
    elif fun == '0':
        break
    else:
        print("输入有误")

        ireak
