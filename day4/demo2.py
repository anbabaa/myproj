class MyExcpt(Exception):
    pass
    def show(self):
        print('hehe')
if __name__ == '__main__':
    me=MyExcpt()
    me.show()
    try:
        raise MyExcpt
    except MyExcpt as e:
        print('raise ,MyExcept')
        e.show()
    pass
    pass
    pass
    print('请输入两个数字，计算除法')
    print('输入q时退出')
    while True:
        print('\t')
        fnum=input('Firet,number')
        if fnum=='q':
            break
        snum=input('Second number:')
        if snum=='q':
            break
    try:
        res=int(fnum)/int(snum)
    except ZeroDivisionError as e:
        pass
    else:
        print('result={0}'.format(res))
    finally:
        pass

