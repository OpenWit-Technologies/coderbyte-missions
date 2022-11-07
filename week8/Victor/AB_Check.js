function ABCheck(str) { 
  
    for (i = 0; i < str.length; i++) {
      if(str[i] === 'a' && str[i+4] === 'b'){
        return true;
      }
    }
    return false;
}
   
// keep this function call here 
console.log(ABCheck(readline()));