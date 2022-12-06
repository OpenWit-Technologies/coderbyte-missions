import math

def bracketcombinatins(num):
    if num == 0 or num == 1:
        return 1
    
    a= math.factorial((2*num))
    b= math.factorial((num + 1))
    c= math.factorial(num)

    ans= a / (b * c)
    return int(ans)


print(bracketcombinatins())