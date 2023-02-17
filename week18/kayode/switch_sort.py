def SwitchSort(arr):
    def loopcounter(start, times, leng, dir):
        if dir == "r":
            end= start + times
            while end >= leng:
                end= end - leng
            return end
        elif dir == "l":
            end= start - times
            while end < 0:
                end= end + leng
            return end
    
    def swapper(swaparr, start, end):
        s= swaparr.copy()
        vals= s[start]
        vale= s[end]
        s[start]= vale
        s[end]= vals
        return s
    

    sarr= arr.copy()
    sarr.sort()
    ope= []
    alen= len(arr)

    if arr == sarr:
        return print(0)
    
    for i in range(alen):
        if arr[i] != sarr[i]:
            ope.append([i, arr[i]])

    
    reslen= []
    for i, j in ope:
        temparr= arr.copy()
        stepcounter= 1
        steprecord= []
        results= []
        
        lend= loopcounter(i, j, alen, "l")
        rend= loopcounter(i, j, alen, "r")
        
        if lend != i:
            lresult= swapper(temparr, i, lend)
            steprecord.append({"steps":stepcounter, "array":lresult})
            results.append(lresult)
        if rend != i:
            rresult= swapper(temparr, i, rend)
            steprecord.append({"steps":stepcounter, "array":rresult})
            results.append(rresult)
        if rend == i and lend == i:
            continue
        # print(steprecord)

        while sarr not in results:
            tempresults= []
            for k in steprecord:
                if k['steps'] == stepcounter:
                    tempresults.append(k)
            
            stepcounter= stepcounter + 1
            
            for p in tempresults:
                tempope= []
                for k in range(alen):
                    if sarr[k] != p['array'][k]:
                        tempope.append([k, p['array'][k]])
                
                for m, n in tempope:
                    lend= loopcounter(m, n, alen, "l")
                    rend= loopcounter(m, n, alen, "r")

                    if lend != m:
                        lresult= swapper(p['array'], m, lend)
                        steprecord.append({"steps":stepcounter, "array":lresult})
                        results.append(lresult)
                    if rend != m:
                        rresult= swapper(p['array'], m, rend)
                        steprecord.append({"steps":stepcounter, "array":rresult})
                        results.append(rresult)
        
        for k in steprecord:
            if k['array'] == sarr:
                reslen.append(k['steps'])
    
    print(reslen)
    return print(min(reslen))




# SwitchSort([3,1,2])
# SwitchSort([1,2,3])
SwitchSort([1,3,4,2])