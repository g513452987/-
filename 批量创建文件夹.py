import os

def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


##################
all_class=['苹果','梨','草莓','菠萝','芒果','西瓜','木瓜','哈密瓜','樱桃','香蕉','火龙果','橘子','葡萄','荔枝','柠檬']
for line in all_class:
    class_name=line.split()[-1]
    mkdir('G:/Python全栈_CSDN/全景图片/图片/'+str(class_name))
