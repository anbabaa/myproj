if __name__ == '__main__':
    m9 = [1, 2, 3, 4]

    for i in m9:
        for h in m9:
            if i < h:
                print(" ", end=" ")
        for k in m9[0:i - 1]:
            print("*", end=" ")

        for j in m9:
            print("*", end=" ")
            if j == i:
                print()
                break
    for i in m9:
        for k in m9:
            print(" ", end=" ")
            if i == k:
                break
        for h in m9:
            if i < h:
                print("*", end=" ")
            if i < h - 1:
                print("*", end=" ")
        print()