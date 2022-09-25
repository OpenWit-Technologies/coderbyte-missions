function FirstFactorial(num) { 

  // code goes here  
  if (num > 0 && num < 18) {
			return num * FirstFactorial(num - 1);
	} else {
      console.log("Sorry the range must be between 1 and 18 and the input must always be an integer.");
			return 1;
	}
}

   
// keep this function call here 
console.log(FirstFactorial(readline()));