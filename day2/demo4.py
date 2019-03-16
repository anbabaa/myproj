import random
if __name__ == '__main__':
    mlist=[1,2,3,4]
    print(type(mlist))
    for l in mlist:
        print("mlist[{0}]={1}".format(l.__index__(),l))
    a=[1,2,3,4]
    for i in a:
        print(i)
    a[0]=10
for i in a:
    print(i)
b=[1,2,3,4]
print("b[{0}]={1}".format(b[2].__index__(), b[2]))
print("b[{0}]={1}".format(b[2].__index__(), b[2]))
c=[1,2,3,4,5,6,7,8,9,0]
print("id->c:",id(c))
d=[1,2,3,4,5,6,7,8,9,0]
print(id(d))
del d
print(d)
print(id(d))
e=[1,2,3,4,5,6,7,8,9,0]
t=2
print('in->',t in e)
print("not in->",t not in e)
f=[1,2,3,4,5,6,7,8,9]
for i in  f:
  print('f[{0}]={1}'.format(i.__index__(),i))
ab=[i for i in range(1,10)]
print('ab=',ab)
ac=[1,2,3,4,5,6,7,8,9,0]
ad=ac[-2:-4:-1]
print('id->ac:',id(ac))
print('id->ad:',id(ad))
ae=[1,2,3,4,5,6,7,8,9,0]
af=[o for o in ae if o%2==0]
print('af=',af)
aj=[1,2,3,4]
ag=[100,200,300,400]
qlist=[m+n for m in aj for n in ag]
print('no if->',qlist)
clist=[m+n for m in aj if m%2==0 for n in ag]
print('with if->',clist)
mlist=[1,2,3,4]
print(type(mlist))
for l in mlist:
    print("mlist[{0}]={1}".format(l.__index__(),l))
a=[1,2,3,4]
for i in a:
    print(i)
a[0]=10
for i in a:
    print(i)
b=[1,2,3,4]
print("b[{0}]={1}".format(b[2].__index__(), b[2]))
print("b[{0}]={1}".format(b[2].__index__(), b[2]))
c=[1,2,3,4,5,6,7,8,9,0]
print("id->c:",id(c))
d=[1,2,3,4,5,6,7,8,9,0]
print(id(d))
del d
print(d)
print(id(d))
e=[1,2,3,4,5,6,7,8,9,0]
t=2
print('in->',t in e)
print("not in->",t not in e)
mlist =[1,2,3,4,'hehe',3.3]
mlen =len(mlist)
print(mlen)
pass
pass
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    print('a[{0}]={1}'.format(i.__index__(),i))
    pass
    mynum = [3, 7, 4, 2]
    random.shuffle(mynum)
    print(mynum)
    mynum.sort(reverse=False)
    print(mynum)
    mynum.reverse()
    print(mynum)
    nset={1,2,3,4,5}
    nfs=frozenset(nfs)
    print('frozenset=',nfs)
    pass
    mset={1,2,3,3,4,4,5,}
    pset={1,2}
    qset=mset-pset
    print('set minus=',qset)


