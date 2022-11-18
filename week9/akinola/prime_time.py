def PrimeTime(num):
  for i in range(2, num):
    if num % i ==0:
      return "false"

  # code goes here
  return "true"

# keep this function call here 
print PrimeTime(raw_input())