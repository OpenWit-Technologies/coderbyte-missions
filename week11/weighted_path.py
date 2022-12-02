# def WeightedPath(strArr):
#     nodeno= int(strArr[0])
#     nodearr= strArr[1:nodeno+1]
#     patharr= strArr[nodeno+1:]
#     patharr2= []
#     startnode= nodearr[0]
#     endnode= nodearr[-1]
#     allpos= []
#     temppos= []
#     posweight= []

#     for i in patharr:
#         patharr2.append(i.split('|'))
    
#     for i in patharr2:
#         if nodearr.index(i[0]) > nodearr.index(i[1]):
#             i[0], i[1] = i[1], i[0]
    
#     # for i,j in enumerate(patharr2):
#     #     for k,l in enumerate(patharr2):
#     #         if (j[0], j[1]) == (l[0], l[1]) and i != k and int(j[2]) < int(l[2]):
#     #             patharr2.pop(k)

#     for i in patharr2:
#         if i[0] == startnode:
#             temppos.append([i])
    
#     for i in temppos:
#         for j in patharr2:
#             if i[-1][1] == j[0]:
#                 x= i.copy()
#                 x.append(j)
#                 temppos.append(x)
    
#     for i in temppos:
#         if i[-1][1] == endnode:
#             allpos.append(i)
    
#     if allpos == []:
#         return print(-1)
    
#     for i in allpos:
#         w= 0
#         for j in i:
#             w= w + int(j[-1])
#         posweight.append(w)
    
#     minindex= posweight.index(min(posweight))
#     leastpath= allpos[minindex]

#     path= ""
#     for i in leastpath:
#         path= path + i[0] + '-'
#     else:
#         path= path + endnode

    

                
#     # print(pospath)
#     # print(nodearr)
#     # print(patharr2)
#     # print(temppos)
#     # print(allpos)
#     # print(posweight)
#     # print(leastpath)
#     return print(path)


def WeightedPath(strArr):
    nodeno= int(strArr[0])
    nodearr= strArr[1:nodeno+1]
    patharr= strArr[nodeno+1:]
    patharr2= []
    startnode= nodearr[0]
    endnode= nodearr[-1]
    allpos= []
    temppos= []
    posweight= []

    for i in patharr:
        patharr2.append(i.split('|'))
    
    for i in patharr2:
        if nodearr.index(i[0]) > nodearr.index(i[1]):
            i[0], i[1] = i[1], i[0]
    
    # for i,j in enumerate(patharr2):
    #     for k,l in enumerate(patharr2):
    #         if (j[0], j[1]) == (l[0], l[1]) and i != k and int(j[2]) < int(l[2]):
    #             patharr2.pop(k)

    for i in patharr2:
        if i[0] == startnode:
            temppos.append([i])
    
    for i in temppos:
        for j in patharr2:
            if i[-1][1] == j[0] or i[-1][1] == j[1]:
                if i[-1][1] == j[0]:
                    y= [j[0], j[1], j[2]]
                elif i[-1][1] == j[1]:
                    y= [j[1], j[0], j[2]]

                if y not in i:
                    x= i.copy()
                    x.append(y)
                    temppos.append(x)
                    
    for i in temppos:
        if i[-1][1] == endnode:
            allpos.append(i)
    
    if allpos == []:
        return print(-1)
    
    for i in allpos:
        w= 0
        for j in i:
            w= w + int(j[-1])
        posweight.append(w)
    
    minindex= posweight.index(min(posweight))
    leastpath= allpos[minindex]

    path= ""
    for i in leastpath:
        path= path + i[0] + '-'
    else:
        path= path + endnode

    return print(path)




# WeightedPath(["4","A","B","C","D","A|B|1","B|D|9","B|C|3","C|D|4"])
WeightedPath(["7","A","B","C","D","E","F","G","A|B|1","A|E|9","B|C|2","C|D|1","D|F|2","E|D|6","F|G|2"])
# WeightedPath(["4","x","y","z","w","x|y|2","y|z|14", "z|y|31"])
# WeightedPath(["8","C","B","A","D","E","F","G","H","C|D|1","D|F|2","G|F|2","G|E|1","E|B|1","H|B|1","C|A|13","B|A|2","C|E|9"])