function ArithGeoII(arr) { 
    var num1 = arr[0];
    var num2 = arr[1];
    var arithmetic = num2 - num1;
    var geometric = num2 / num1;
   
    var isArithmetic = true;
    var isGeometric = true;
    
    for (var i = 0; i < arr.length-1; i++) {
        var first = arr[i];
        var second = arr[i+1];
        
        if (second / first !== geometric) {
            isGeometric = false;
        }
      
        if ((second - first) !== arithmetic) {
            isArithmetic = false;
        } 
        
    }
    
    if (isGeometric) {
        return 'Geometric'
    } else if (isArithmetic) {
        return 'Arithmetic'
    } else {
        return -1
    }
}
   
// keep this function call here 
ArithGeoII(readline());