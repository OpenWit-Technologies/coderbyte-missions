function ArithGeo(arr) { 
    
    var arithDiff = arr[1] - arr[0];
    var geomDiff = arr[1] / arr[0];
  
    var multiples;

  for (var i=1; i<arr.length-1; i++) {
      if (arr[i+1] - arr[i] == arithDiff) {
          if (multiples == "Geometric") {
              return -1;
          }
          multiples = "Arithmetic";
          
      } else if (arr[i+1] / arr[i] == geomDiff) {
          if (multiples == "Arithmetic") {
              return -1;
          }
          multiples = "Geometric";
        } else {
            return -1;
        }
      }
  
  return multiples; 
         
}

ArithGeo(readline());