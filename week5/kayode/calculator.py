import re

def string_calc(string):
    #search through the string and keep digits or operators in a list
    l1= re.findall('\d+|[/ + \- *]', string)
    #convert all string digits to integers
    for i in range(len(l1)):
        if l1[i].isnumeric():
            l1[i]= int(l1[i])
    
    l2= l1.copy()
    for i in range(len(l1)):
        if l1[i] == "-" and type(l1[i-1]) != int and type(l1[i+1]) == int:
            l2[i:i+2]= [-l2[i+1]]
        if l1[i] == "-" and i-1 < 0 and type(l1[i+1]) == int:
            l2[:i+2]= [-l2[i+1]]

    l1= l2
    
    #check for operators in the list and perform operations on their adjacent elements
    while "/" in l1:
        i= l1.index("/")
        l1[i-1:i+2]= [l1[i-1]/l1[i+1]]
    while "*" in l1:
        i= l1.index("*")
        l1[i-1:i+2]= [l1[i-1]*l1[i+1]]
    while "+" in l1:
        i= l1.index("+")
        l1[i-1:i+2]= [l1[i-1]+l1[i+1]]
    while "-" in l1:
        i= l1.index("-")
        l1[i-1:i+2]= [l1[i-1]-l1[i+1]]

    return str(int(l1[0]))


def brac_calc(matchobj):
    #retrieve the matched string from the string result
    string= matchobj.group(0)
    #remove the brackets
    string2= re.sub("[( )]", "", string)
    #evaluate the expression and return a string version of the answer
    return str(string_calc(string))




def calculator(string):
    #check if there are brackets in the mathematical expression
    if ")(" in string:
        string= re.sub("\)\(", ")*(", string)
    if "(" in string:
        #if there are brackets, perform regular expression to evaluate the content of the bracket
        brcks= re.sub("\(\d[+ \- * /]\d\)", brac_calc, string)
        while "(" in brcks:
            brcks= re.sub("\(\d[+ \- * /]\d\)", brac_calc, brcks)
        #then calculate the string result
        return string_calc(brcks)
    else:
        #else call string_calc function to calculate the expression
        return string_calc(string)
        



print(calculator("-3+1"))
