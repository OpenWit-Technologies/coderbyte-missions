import math
from fractions import Fraction

# def IntersectingLines(arr):
#     arr2= []
#     arr3= []
#     plot1= []
#     plot2= []
#     intersect= []

#     for i in arr:
#         x= i.replace("(", "").replace(")", "").split(',')
#         arr2.append(x)
    
#     for i,j in arr2:
#         k= int(i)
#         l= int(j)
#         arr3.append([k,l])
    
#     l1x1= arr3[0][0]
#     l1y1= arr3[0][1]
#     l1x2= arr3[1][0]
#     l1y2= arr3[1][1]
#     l2x1= arr3[2][0]
#     l2y1= arr3[2][1]
#     l2x2= arr3[3][0]
#     l2y2= arr3[3][1]

#     m1= (l1y2 - l1y1) / (l1x2 - l1x1)
#     m2= (l2y2 - l2y1) / (l2x2 - l2x1)
#     b1= l1y1 - (m1 * l1x1)
#     b2= l2y1 - (m2 * l2x1)

#     if (l1x1 > 0 and l1x2 > 0):
#         if l1x1 > l1x2:
#             dif1= abs(l1x1) - abs(l1x2)
#         elif l1x2 > l1x1:
#             dif1= abs(l1x2) - abs(l1x1)
#     elif l1x1 < 0 and l1x2 < 0:
#         if l1x1 > l1x2:
#             dif1= abs(l1x2) - abs(l1x1)
#         elif l1x2 > l1x1:
#             dif1= abs(l1x1) - abs(l1x2)
#     else:
#         dif1= abs(l1x1) + abs(l1x2)
    
#     if (l2x1 > 0 and l2x2 > 0):
#         if l2x1 > l2x2:
#             dif2= abs(l2x1) - abs(l2x2)
#         elif l2x2 > l2x1:
#             dif2= abs(l2x2) - abs(l2x1)
#     elif l2x1 < 0 and l2x2 < 0:
#         if l2x1 > l2x2:
#             dif2= abs(l2x2) - abs(l2x1)
#         elif l2x2 > l2x1:
#             dif2= abs(l2x1) - abs(l2x2)
#     else:
#         dif2= abs(l2x1) + abs(l2x2)
    
#     counter1= 0
#     counter2= 0
#     if l1x1 < l1x2:
#         s1= l1x1
#     else:
#         s1= l1x2
    
#     if l2x1 < l2x2:
#         s2= l2x1
#     else:
#         s2= l2x2

#     for i in range(int(dif1*10000)):
#         d= s1 + counter1
#         e= round(d, 5)
#         c= (e * m1) + b1
#         f= round(c, 5)
#         plot1.append([e, f])
#         counter1= counter1 + 0.00010000000000000000000000000
    
#     for i in range(int(dif2*10000)):
#         d= s2 + counter2
#         e= round(d, 5)
#         c= (e * m2) + b2
#         f= round(c, 5)
#         plot2.append([e, f])
#         counter2= counter2 + 0.0001000000000000000000000000
    
#     for i in plot1:
#         if i in plot2:
#             intersect.append(i)

#     print(plot1)
#     print(plot2)
#     if intersect == []:
#         return print("no intersection")
#     else:
#         ans= "(" + str(Fraction(intersect[0][0]).limit_denominator(10000)) + "," + str(Fraction(intersect[0][1]).limit_denominator(10000)) + ")"
#         print(ans)

#     # print(arr2)
#     # print(arr3)
#     # print(m1, m2)
#     # print(dif1, dif2)
#     # print(plot1)
#     # print(plot2)


def IntersectingLines(arr):
    arr2= []
    arr3= []
    plot1= []
    plot2= []
    intersect= []

    for i in arr:
        x= i.replace("(", "").replace(")", "").split(',')
        arr2.append(x)
    
    for i,j in arr2:
        k= int(i)
        l= int(j)
        arr3.append([k,l])
    
    l1x1= arr3[0][0]
    l1y1= arr3[0][1]
    l1x2= arr3[1][0]
    l1y2= arr3[1][1]
    l2x1= arr3[2][0]
    l2y1= arr3[2][1]
    l2x2= arr3[3][0]
    l2y2= arr3[3][1]

    try:
        m1= (l1y2 - l1y1) / (l1x2 - l1x1)
    except ZeroDivisionError:
        ix= l1x2
        m1= "undefined"
    
    try:
        m2= (l2y2 - l2y1) / (l2x2 - l2x1)
    except ZeroDivisionError:
        ix= l2x2
        m2= "undefined"
    
    if m1 != "undefined":
        b1= l1y1 - (m1 * l1x1)
    if m2 != "undefinfed":
        b2= l2y1 - (m2 * l2x1)

    try:
        if m1 != "undefined" and m2 != "undefined":
            ix= (b2 - b1) / (m1 - m2)
    except ZeroDivisionError:
        return print("no intersection")
    
    if m1 != "undefined":
        iy= (ix * m1) + b1
    else:
        iy= (ix * m2) + b2

    ans= "(" + str(Fraction(ix).limit_denominator(1000)) + "," + str(Fraction(iy).limit_denominator(1000)) + ")"
    return print(ans)



# IntersectingLines(["(9,-2)","(-2,9)","(3,4)","(10,11)"])
# IntersectingLines( ["(3,0)","(1,4)","(0,-3)","(2,3)"])
# IntersectingLines(["(0,15)","(3,-12)","(2,1)","(13,7)"])
# IntersectingLines(["(1,2)","(3,4)","(-5,-6)","(-7,-8)"])
# IntersectingLines(["(0,0)","(0,-1)","(1,1)","(0,1)"])
IntersectingLines(["(1,-1)","(1,1)","(-5,-5)","(-7,-7)"])