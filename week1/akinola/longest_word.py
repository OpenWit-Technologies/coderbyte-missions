function LongestWord(sen) { 
  words = sen.match(/\w+/g);
  
  longest = words[0];

  for(a=0; a<words.length; a++){
    if(words[a].length > longest.length) {
      longest = words[a];
    }
  }
 // code goes here  
  return longest; 

}
   
// keep this function call here 
console.log(LongestWord(readline()));