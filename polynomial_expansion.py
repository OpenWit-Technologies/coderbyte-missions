import re

# def polynomial_expansion(strParam):
#     letter= re.search("[a-z]|[A-Z]", strParam).group()
#     m1= strParam.split(')(')
#     m2= []
#     tempsol= []
#     for i,j in enumerate(m1):
#         ns= j.replace('(', '').replace(')', '')
#         m1[i]= ns
    
#     for i in m1:
#         t1= re.match("(-|/+|)\d+\w(\^)(-|/+|)\d+", i)
#         if t1 == None:
#             t1= re.match("(-|/+|)\d+\w", i)
#         if t1 == None:
#             t1= re.match("(-|/+|)\d+", i)
        
#         t2= i.replace(t1.group(), '')
#         if t2 != '':
#             m2.append([t1.group(), t2])
#         else:
#             m2.append([t1.group()])

#     for i in m2[0]:
#         if re.match("(-|/+|)\d+\w(\^)(-|/+|)\d+", i):
#             td2= int(re.search("((-|/+|)\d+)$", i).group())
#             td1= int(re.match("(-|/+|)\d+", i).group())
#         elif re.match("(-|/+|)\d+\w", i):
#             td1= int(re.match("(-|/+|)\d+", i).group())
#             td2= 1
#         else:
#             td1= int(i)
#             td2= 0
        
#         for j in m2[1]:
#             if re.match("(-|/+|)\d+\w(\^)(-|/+|)\d+", j):
#                 ed2= int(re.search("((-|/+|)\d+)$", j).group())
#                 ed1= int(re.match("(-|/+|)\d+", j).group())
#             elif re.match("(-|/+|)\d+\w", j):
#                 ed1= int(re.match("(-|/+|)\d+", j).group())
#                 ed2= 1
#             else:
#                 ed1= int(j)
#                 ed2= 0
            
#             ttd1= ed1 * td1
#             ttd2= ed2 + td2
#             tempsol.append([ttd1, ttd2])
    
#     for i,j in enumerate(tempsol):
#         for k, l in enumerate(tempsol):
#             if j[1] == l[1] and k != i:
#                 tempsol[i][0]= tempsol[i][0] + tempsol[k][0]
#                 tempsol.pop(k)
#                 break

#     def sortcriteria(e):
#         return e[1]
#     tempsol.sort(key=sortcriteria, reverse=True)
    
#     solu= ""
#     for i in tempsol:
#         if solu != "" and i[0] > 0:
#             solu= solu + "+"
#         if i[1] > 1 or i[1] < 0:
#             if i[0] == 1:
#                 solu= solu + letter + "^" + str(i[1])
#             else:
#                 solu= solu + str(i[0]) + letter + "^" + str(i[1])
#         elif i[1] == 1:
#             if i[0] == 1:
#                 solu= solu + letter
#             else:
#                 solu= solu + str(i[0]) + letter
#         elif i[1] == 0:
#             solu= solu + str(i[0])



#     print(m1)
#     print(m2)
#     print(tempsol)
#     print(solu)
       

def polynomial_expansion(strParam):
    letter= re.search("[a-z]|[A-Z]", strParam).group()
    m1= strParam.split(')(')
    m2= []
    tempsol= []
    for i,j in enumerate(m1):
        ns= j.replace('(', '').replace(')', '')
        m1[i]= ns
    
    for i in m1:
        term= i
        termlist= []
        
        while term != "":
            t= re.match("(-|\+|)\d+\w(\^)(-|/+|)\d+", term)
            if t == None:
                t= re.match("(-|\+|)\d+\w", term)
            if t == None:
                t= re.match("(-|\+|)\d+", term)
            termlist.append(t.group())
            term= term.replace(t.group(), '', 1)
        
        m2.append(termlist)

    for i in m2[0]:
        if re.match("(-|\+|)\d+\w(\^)(-|/+|)\d+", i):
            td2= int(re.search("((-|\+|)\d+)$", i).group())
            td1= int(re.match("(-|\+|)\d+", i).group())
        elif re.match("(-|\+|)\d+\w", i):
            td1= int(re.match("(-|\+|)\d+", i).group())
            td2= 1
        else:
            td1= int(i)
            td2= 0
        
        for j in m2[1]:
            if re.match("(-|\+|)\d+\w(\^)(-|/+|)\d+", j):
                ed2= int(re.search("((-|\+|)\d+)$", j).group())
                ed1= int(re.match("(-|\+|)\d+", j).group())
            elif re.match("(-|\+|)\d+\w", j):
                ed1= int(re.match("(-|\+|)\d+", j).group())
                ed2= 1
            else:
                ed1= int(j)
                ed2= 0
            
            ttd1= ed1 * td1
            ttd2= ed2 + td2
            tempsol.append([ttd1, ttd2])
    
    for i,j in enumerate(tempsol):
        for k, l in enumerate(tempsol):
            if j[1] == l[1] and k != i:
                tempsol[i][0]= tempsol[i][0] + tempsol[k][0]
                tempsol.pop(k)
                break

    def sortcriteria(e):
        return e[1]
    tempsol.sort(key=sortcriteria, reverse=True)
    
    solu= ""
    for i in tempsol:
        if solu != "" and i[0] > 0:
            solu= solu + "+"
        if i[1] > 1 or i[1] < 0:
            if i[0] == 1:
                solu= solu + letter + "^" + str(i[1])
            else:
                solu= solu + str(i[0]) + letter + "^" + str(i[1])
        elif i[1] == 1:
            if i[0] == 1:
                solu= solu + letter
            else:
                solu= solu + str(i[0]) + letter
        elif i[1] == 0:
            solu= solu + str(i[0])



    print(m1)
    print(m2)
    print(tempsol)
    print(solu)



# polynomial_expansion("(1x)(2x^-2+1)")
# polynomial_expansion("(2x^2+4)(6x^3+3)")
# polynomial_expansion("(2x^2+4)(6x^2+3)")
# polynomial_expansion("(1x^5-4x^2+3)(2x^2+3)")
# polynomial_expansion("(1x)(2x^-2+1)")
polynomial_expansion("(-1p^1+3)(-1p^2-1p^2)")
