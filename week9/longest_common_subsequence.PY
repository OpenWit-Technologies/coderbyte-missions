from itertools import combinations

def LCS(strArr):
    first= strArr[0]
    second= strArr[1]
    
    firstsubs= []
    secondsubs= []
    for i in range(len(first)):
        comb1= list(combinations(first, i))
        comb2=[]
        for j in comb1:
            comb2.append(''.join(j))
        firstsubs.extend(comb2)

    
    for i in range(len(second)):
        comb3= list(combinations(second, i))
        comb4=[]
        for j in comb3:
            comb4.append(''.join(j))
        secondsubs.extend(comb4)
    
    firstsubs.remove('')
    secondsubs.remove('')
    if firstsubs == []:
        firstsubs.append(first)
    if secondsubs == []:
        secondsubs.append(second)
    
    sublength= 0

    for i in firstsubs:
        for j in secondsubs:
            if i == j:
                if len(i) > sublength:
                    sublength= len(i)
    

    print(sublength)



# LCS(['bcacb', 'aacabb'])
LCS(['a', 'aa'])
# LCS(['c', 'b'])