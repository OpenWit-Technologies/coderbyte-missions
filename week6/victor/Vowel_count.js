function VowelCount(str) { 

    let vowels  =  str.match(/[aeiouAEIOU]/g);
    return vowels.length; 
           
  }
     
  // keep this function call here 
  VowelCount(readline());