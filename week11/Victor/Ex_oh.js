function ExOh(str) { 

    var xArray = str.match(/x/g);
    var oArray = str.match(/o/g);
    
     if (!xArray || !oArray) {
         return false;
     }
     if (xArray.length === oArray.length) {
         return true;
     }
     return false; 
            
   }
     
   
   console.log(ExOh(readline()));