def counting_anagrams(arr):
    arr2= arr.split()
    anna= 0

    for i,j in enumerate(arr2):
        for k,l in enumerate(arr2):
            if j == l and i != k:
                arr2.pop(k)
    
    for i in arr2:
        for j in arr2:
            if len(i) == len(j):
                if i != j:
                    for k in i:
                        if k in j:
                            i.replace(k, '')
                        else:
                            break
                    else:
                        arr2.remove(j)
                        anna= anna + 1
    
    print(anna)



# counting_anagrams("aa aa odg dog gdo")
counting_anagrams("a c b c run urn urn")