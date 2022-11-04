from itertools import combinations

def parallelsumns(arr):
    slen= len(arr) // 2
    arrset= []
    sumset= []
    sumpairs= []
    result= -1

    #create all possible list combinations of the elements of the given list of length equal to half of the given list
    setcomb= list(combinations(arr, slen))
    
    #append the sum of each combination of elements as well as the combination themselves to new lists
    for i in setcomb:
        arrset.append(i)
        sumset.append(sum(i))
    
    #because each combination of elements returned by the combination function is a tuple, create a new list where each tuple is converted to a list so that rather than a list of tuples, we have a list of lists.
    arrset2= [list(i) for i in arrset]
    
    #loop throught the list of combinations and if any two combinations are the same when each combination is sorted, delete one of those two combinations as well as it's sum in the list of sums. This is to ensure each combination in the list of combinations is completely unique
    for i,j in enumerate(arrset2):
        for k,l in enumerate(arrset2):
            if i==k:
                continue
            else:
                if j==l:
                    arrset2.pop(k)
                    sumset.pop(k)
                elif sorted(j) == sorted(l):
                    arrset2.pop(k)
                    sumset.pop(k)
    

    #loop through the list of sums that contains the sums of each combination. If any two sums are the same, combine those two combinations that make up the sums into a single list and then append that list into a new list to create a list of paired combinations
    for i,j in enumerate(sumset):
        for k,l in enumerate(sumset):
            if i == k:
                continue
            else:
                if j == l:
                    sumpairs.append([arrset2[i], arrset2[k]])
    
    
    #loop through the list of paired combinations, for each element of the list, combine the paired combinations into one single list, sort the list and then compare with a sorted version of the original list. If the two list are the same, append the paired combination into a new list.
    sumpairs2= []
    for i, j in enumerate(sumpairs):
        a= j[0].copy()
        b= j[1].copy()
        a.extend(b)
        if sorted(a) == sorted(arr):
            sumpairs2.append(sumpairs[i])
    

    #if the new list is empty, it means there are no paired combinations that return the required value as none of the combined paired combinations is equal to the original provided list
    if sumpairs2 == []:
        print(result)
        return result

    #as only one set of paired combinations will be equal to the origninal list when combined, sort the elements of each combination pair in ascending order
    sumpairs3= sumpairs2[0]
    for i in range(len(sumpairs3)):
        sumpairs3[i]= sorted(sumpairs3[i])

    #sort the combination pairs themselves
    sumpairs3= sorted(sumpairs3)

    #convert each element of each combination in the combination pair to strings and then concatenate them the two combinations into a single string.
    result= ','.join([str(i) for i in sumpairs3[0]]) + ','  + ','.join([str(i) for i in sumpairs3[1]])

    print(result)



parallelsumns([2,3,1,9,3,4,4,4])