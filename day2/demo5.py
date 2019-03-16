if __name__ == '__main__':
    mlist =[1,2,3,4,'hehe',3.3]
    mlen =len(mlist)
    print(mlen)
    pass
    pass
    a=[1,2,3,4,5,6,7,8,9]
    for i in a:
        print('a[{0}]={1}'.format(i.__index__(),i))
        nset={1,2,3,3,4,4,5}
        pset={1,2}
        nis=nset.issuperset(pset)
        print('set.issupperset=',nis)
        pass
    pass
    nset={1,2,3,3,4,4,5}
    pset={1,2,7}
    qset=nset.union(pset)
    print('set.union=',qset)
    pass
    nset = {1,2,3,3,4,4,5,}
    pset={1,2}
    qset = nset.difference(pset)
    pset('difference=',qset)
