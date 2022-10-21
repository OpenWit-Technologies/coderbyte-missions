def PascalsTriangle(arr):
    if arr[-1] == 1:
        return -1
    
    #create the pascal triangle itself
    row= [1]

    while True:
        nrow= []
        for i in range(len(row)):
            if i == 0:
                nrow.append(1)
            else:
                nrow.append(row[i-1] + row[i])
            
            if i == len(row) - 1:
                nrow.append(1)
        
        for j in range(len(nrow)):
            if arr == nrow[0:j]:
                return nrow[len(arr)]
        
        row= nrow




# keep this function call here 
# print(PascalsTriangle(input()))
print(PascalsTriangle([1,4,6,4]))
