function BracketMatcher(str){
    var left=0;
    var right=0;
    for(var i=0; i<str.length; i++){
        if(str[i]==="("){
            left++;
        }
        else if(str[i]===")"){
            right++;
        }
    }
if(right===left){
    return 1;
  }
    else{
      return 0;
    }
}
   
// keep this function call here 
console.log(BracketMatcher(readline()));