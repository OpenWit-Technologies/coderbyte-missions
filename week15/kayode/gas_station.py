def gas_station(arr):
    stops= int(arr.pop(0))
    route= []
    result1= []
    result2= []
    for i in arr:
        s= i.split(':')
        route.append([int(j) for j in s])
    
    for i,j in enumerate(route):
        fuel= 0
        run= 0
        
        for k in range(stops):
            ind= i + k
            if ind >= stops:
                ind= ind - stops
            fuel= route[ind][0] + fuel
            if route[ind][1] <= fuel:
                fuel= fuel - route[ind][1]
                run= run + 1
            else:
                result1.append([i, False])
                break
                
        
        if run == stops:
            result1.append([i, True])
    
    for i in result1:
        if i[1]:
            result2.append(i[0] + 1)
    
    if result2 == []:
        return print("impossible")
    else:
        return print(min(result2))


gas_station(['4', '3:1', '2:2', '1:2', '0:1'])
# gas_station(["4","1:1","2:2","1:2","0:1"])
# gas_station(["4","0:1","2:2","1:2","3:1"])