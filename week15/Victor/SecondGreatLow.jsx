function SecondGreatLow(arr) { 

    if (arr.length === 2) {
          arr.sort(function(a,b) {return a - b});
          return arr[1] + " " + arr[0];
     }
      
    var values = arr.filter(function(num, pos) {
      return arr.indexOf(num) == pos;
    });
      
    if (values.length > 2) {
      values.sort(function(a, b){return a-b});
       return values[1] + " " + values[values.length - 2]; 
    }
    else {
      return values[1] + " " + values[0];
    }
  
  }
  
  console.log(SecondGreatLow(readline()));