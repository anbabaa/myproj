import random
def checkSex() :
    name = input("请输入姓名：")
    sex = input("请输入性别：")
    mlist = ["男","man","Mr.","boy"]
    nlist = ["女","woman","Mrs.","girle"]
    pass
    if sex in mlist :
        print("{0}先生你好".format(name))
    elif sex in nlist :
        print("{0}女士你好".format(name))
    pass
def two():
    mlist = [random.randint(1,100) for i in range(10)]
    nlist = [random.randint(1,150) for i in range(15)]
    mset = set(mlist)
    nset = set(nlist)
    print(mlist)
    print(nlist)
    print("并集之后：")
    gset = set(mset | nset)
    glist = list(gset)
    print(glist)
    pass
    pass
def em():
    email = input("请输入邮箱：")
    mlist = list(email)
    if '@' in mlist :
        nlist = list(email.split('@'))
        nlen = len(nlist[0])
        if nlen >=6 :
            if '.' not in nlist[1] :
                print("少了.")
            else :
                print("{0}合法".format(email))
        else :
            print("姓名长度不能少于6位")

    else :
        print("没有@")
    pass
    pass
def huiwen() :
    str = input("请输入一个数字字符串：")
    if len(str)%2 == 1 :
        str1 = str[::-1]
        if str1 == str :
            print("是回文数")
        else :
            print("不是回文数")
    else :
        print("不是回文数")


