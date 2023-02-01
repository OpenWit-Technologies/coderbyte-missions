def SymmetricMatrix(strArr):
    mrows= []
    mtrows= []
    temprow= []
    lencheck= []

    if "<>" not in strArr:
        return print("not possible")

    for i in strArr:
        if i == "<>":
            mrows.append(temprow)
            temprow= []
            continue
        temprow.append(i)
    else:
        mrows.append(temprow)
        temprow= []
    
    for i in mrows:
        lencheck.append(len(i))

    print(lencheck)
    print(lencheck.count(lencheck[0]))
    if lencheck.count(lencheck[0]) != lencheck[0] or lencheck.count(lencheck[0]) != len(lencheck):
        return print("not possible")

    loopcount= 0
    indexcount= 0
    while loopcount < lencheck[0]:
        for i in mrows:
            temprow.append(i[indexcount])
        else:
            mtrows.append(temprow)
            temprow= []

        loopcount= loopcount + 1
        indexcount= indexcount + 1

    if mrows == mtrows:
        return print("symmetric")
    else:
        return print("not symmetric")

    


# SymmetricMatrix(["1","0","1","<>","0","1","0","<>","1","0","1"])
# SymmetricMatrix(["5","0","<>","0","5"])
# SymmetricMatrix(["1","2","4","<>","2","1","1","<>","-4","1","-1"])
# SymmetricMatrix(["21","41","81","161"])
# SymmetricMatrix(["-6","1","-6","<>","-1","-1","-1"])
# SymmetricMatrix(["1","2","4","<>","2","1","1","<>","1","1","1","<>","100"])