if __name__ == '__main__':
    nstr='woaixuexi niaibuaixuexi'
    nset =set(nstr)
    for i in nset:
        if nset.count(i)>=2:
            print(i,nset.count(i))