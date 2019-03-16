if __name__ == '__main__':
    pass
    try:
        print(5/0)
    except ZeroDivisionError as e:
        pass
        print('ZeroDivisionError')
        print(e)
    print('good',end='')

    print('输入两个数字，计算除法')
    print('出入q退出')
    pass
    while True:
        print('\t')
        fnum = input('First number:')
        if fnum=='q':
            break
        snum = input('Second number:')
        if snum=='q':
            break
        res=int(fnum)/int(snum)
        print('result={0}'.format(res))
        pass
    print('请输入两个数，计算除法')
    print('输入q退出')
    while True:
        print('\t')
        cnum=input('First number:')
        if cnum=='q':
            break

        vnum=input('Second number:')
        if vnum=='q':
            break
        try:
            res=int(cnum)/int(vnum)
        except ZeroDivisionError as e:
            print('division error')
        else:
            print('result={0}'.format(res))
        finally:
            print('在这里处理一些收尾工作，如果有')
    pass
    try:
        f=open('good.text','r')
        f.close()
    except:
        pass
    def mfun(v):
        if v==0:
            raise Exception('good')
    try:
        mfun(0)
    except Exception as e:
        print('excetp->{0}'.format(e))
        pass
    print('good')
    pass
    # class myException(valueError):
    #     pass
    # try:
    #     print('before raise exception')
    #     raise  myException
    #     print('after raise exception')
    # except myException as me:
    #     print('catch myException')



