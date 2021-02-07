for i in range(2, 13):
    print("------------")
    print( i )
    for j in range(1, 12 + 1):
        print("%d * %d : %d" % (i, j, i * j))