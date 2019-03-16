if __name__ == '__main__':
    mset=set()
    print('mset type=',type(mset))
    pass
    mdict={'name':'good','age':'18'}
    pass
    ndict=dict()
    print(type(mdict))
    print(type(ndict))
    pass
    mytuple=(1,2,3,4,5,6)
    #mytuple[0]=1
    print(mytuple)
    print('mytuple[{1}]={0}'.format(mytuple[1],4))
    for t in mytuple:
        print('mytuple->',t)
    pass
    ntuple=mytuple[0:6:1]
    print('ntuple=',ntuple)
    pass
    ctuple=mytuple
    print('id of +=ctuple->',id(ctuple))
    print('id of +=mtuple->',id(mytuple))
    pass
    ctuple+=mytuple
    print('id of += ntuple->',id(ctuple))
    pass
    print('\n'.join([''.join([('Love'[(x - y) % len('Love')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
            x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

