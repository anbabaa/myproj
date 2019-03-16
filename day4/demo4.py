if __name__ == '__main__':
    try:
        mfile=open(r'C:\Userss\Administrator\PycharmProjects\myproj\day4\a.c')
    except OSError:
        print('oserror')
    except Exception:
        print('Exception')
    else:
        mfile.close()
    pass
    f=open(r'./text.txt','w')
    f.close()
    pass
    mlist=['gun','dan','u can u up']
    mfile=open(r'C:\Userss\Administrator\PycharmProjects\myproj\day4\a.c','w')
    mbool=mfile.writable()
    mwr=mfile.write('gundan')
    print('mwr={mwrkey}'.format(mwrkey=mwr))
    mfile.writelines(mlist)
    mfile.close()
    pass
    a=open(r'./text.txt','w')
    len=a.write('ni qin ai de an baba a')
    print(len)
    a.close()
    pass
    afile=open(r'C:\Userss\Administrator\PycharmProjects\myproj\day4\a.c')
    abool=afile.readable()
    print(abool)
    val = afile.read()
    aline=afile.readline()
    alist = afile.readlines()
    afile.close()
    pass
    pass
    pass
    pass
    c=open(r'./text.txt','r')
    cbuf=c.read(1024)
    print('cbuf={0}'.format(cbuf))
    c.close()
    pass
    pass
    pass
    afile = open(r'C:\Userss\Administrator\PycharmProjects\myproj\day4\a.c')
    abool = afile.readable()
    print(abool)
    val = afile.read()
    aline = afile.readline()
    alist = afile.readlines()
    afile.close()
    pass
    mlist=['gun','dan','u can u up']
    mfile=open(r'C:\Userss\Administrator\PycharmProjects\myproj\day4\a.c','w')
    mbool=mfile.writable()
    mwr=mfile.write('gundan')
    print('mwr={mwrkey}'.format(mwrkey=mwr))
    mfile.writelines(mlist)
    mfile.close()
    pass
    pass

    d=open(r'./text.txt','r')
    while True:
        cbuf=d.readline()
        if cbuf.__len__()==0:
            break
            print('line={0}'.format(cbuf))
    d.close()
    pass
    pass
    pass
    e=open(r'./text.txt','r')
    fbufs=e.readline()
    for l in fbufs:
        print(l)
    e.close()
    pass
    pass
    mlist = ['gun', 'dan', 'u can u up']
    mfile = open(r'C:\Userss\Administrator\PycharmProjects\myproj\day4\a.c', 'w')
    mbool = mfile.writable()
    mwr = mfile.write('gundan')
    print('mwr={mwrkey}'.format(mwrkey=mwr))
    mfile.writelines(mlist)
    mfile.close()
    pass
    mlist=['gun','dan','u can u up']
    mfile=open(r'C:\Userss\Administrator\PycharmProjects\myproj\day4\a.c','w')
    mbool=mfile.writable()
    mwr=mfile.write('gundan')
    print('mwr={mwrkey}'.format(mwrkey=mwr))
    mfile.writelines(mlist)
    mfile.close()
    pass
    j=open(r'./text.txt','r')
    while True:
        pass
