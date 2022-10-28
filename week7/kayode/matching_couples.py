def MatchingCouples(arr):
    x= arr[2]//2
    choicefactorial= x
    boyinitial= arr[0]
    girlinitial= arr[1]
    boyfactorial= boyinitial
    girlfactorial= girlinitial
    boydifference= boyinitial - x
    girldifference= girlinitial - x

    for i in range(arr[0]-1,0,-1):
        boyfactorial= boyfactorial * i
    
    for i in range(arr[1]-1,0,-1):
        girlfactorial= girlfactorial * i
    
    for i in range(choicefactorial-1,0,-1):
        choicefactorial= choicefactorial * i
    
    for i in range(boydifference-1, 0, -1):
        boydifference = boydifference * i
    
    for i in range(girldifference-1, 0, -1):
        girldifference = girldifference * i
    
    boycombination = boyfactorial/(choicefactorial * boydifference)
    girlcombination = girlfactorial/(choicefactorial * girldifference)

    matching= boycombination * girlcombination * x

    print(int(matching))
    

MatchingCouples([10,5,4])