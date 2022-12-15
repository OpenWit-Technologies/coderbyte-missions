def ArrayJumping(arr):
    def loopcounter(start, times, leng, dir):
        if dir == "r":
            end= start + times
            while end >= leng:
                end= end - leng
            return end
        elif dir == "l":
            end= start - times
            while abs(end) >= leng:
                end= end + leng
            return end
    
    alen= len(arr)
    amax= max(arr)
    amaxin= arr.index(amax)

    endr= loopcounter(amaxin, amax, alen, "r")
    endl= loopcounter(amaxin, amax, alen, "l")
    dectree= [{"index":amaxin, "value":amax, "right":endr}, {"index":amaxin, "value":amax, "left":endl}]
    torun= [endr, endl]

    while True:
        torun2= []
        for i in torun:
            times= arr[i]
            endr= loopcounter(i, times, alen, "r")
            endl= loopcounter(i, times, alen, "l")

            for j in dectree:
                if j['index'] == endr:
                    if endr == amaxin:
                        dectree.append({"index":i, "value":times, "right":endr})
                        break
                    else:
                        break
            else:
                torun2.append(endr)
                dectree.append({"index":i, "value":times, "right":endr})
            
            for j in dectree:
                if j['index'] == endl:
                    if endl == amaxin:
                        dectree.append({"index":i, "value":times, "left":endl})
                        break
                    else:
                        break
            else:
                torun2.append(endl)
                dectree.append({"index":i, "value":times, "left":endl})
        else:
            torun= torun2
        
        if torun2 == []:
            counter= 0
            for i in dectree:
                if i.get('right') == amaxin or i.get('left') == amaxin:
                    counter= counter + 1
            
            if counter < 1:
                return print(-1)
            else:
                temptrace= []
                trace=[]
                for i in dectree:
                    if i.get('right') == amaxin or i.get('left') == amaxin:
                        temptrace.append([i])
                
                for i in temptrace:
                    if i[-1]['index'] != amaxin:
                        for j in dectree:
                            if j.get('right') == i[-1]['index'] or j.get('left') == i[-1]['index']:
                                y= []
                                y.extend(i)
                                y.append(j)
                                temptrace.append(y)
                
                for i in temptrace:
                    if (i[0].get('right') == amaxin or i[0].get('left') == amaxin) and i[-1]['index'] == amaxin:
                        trace.append(len(i))

                # return print(dectree, temptrace, trace, sep="\n\n")
                return print(min(trace))


        

ArrayJumping([2,3,5,6,1])
# ArrayJumping([1,2,3,4,2])
# ArrayJumping([1,7,1,1,1,1])