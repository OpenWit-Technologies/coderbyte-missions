def MatrixDeterminant(strArr):
    def matrix_calc(r, length):
        if length > 2:
            detrow= []

            #recreate the rows first
            tr= r.copy()
            fr= tr.pop(0)
            print(tr)
            print(length)
            for i in range(length):
                tr2= tr.copy()
                tr2len= len(tr2)
                tr3= []
                for j in range(tr2len):
                    mrow= tr2[j].copy()
                    mrow.pop(i)
                    tr3.append(mrow)
                tr3len= len(tr3)
                detrow.append(matrix_calc(tr3, tr3len))
            
            determinant= 0
            for i, j in enumerate(fr):
                if i % 2 == 0:
                    determinant= determinant + (j * detrow[i])
                else:
                    determinant= determinant - (j * detrow[i])
            
            return determinant
        elif length == 2:
            determinant= (r[0][0] * r[1][1]) - (r[0][1] * r[1][0])
            return determinant


    
    srows= []
    temp= []
    rows= []
    for i in strArr:
        if i == "<>":
            srows.append(temp)
            temp= []
        else:
            temp.append(i)
    else:
        srows.append(temp)
    
    rowlen= len(srows[0])
    if len(srows) != rowlen:
        return print(-1)
    for i in srows:
        if len(i) != rowlen:
            return print(-1)

    for i in srows:
        temprow= []
        for j in i:
            temprow.append(int(j))
        rows.append(temprow)

    
    # print(srows)
    print(rows)
    print(matrix_calc(rows, rowlen))
        

# MatrixDeterminant(["5","0","<>","0","5"])
# MatrixDeterminant(["1","2","4","<>","2","1","1","<>","4","1","1"])
MatrixDeterminant(["2","1","<>","4","1"])