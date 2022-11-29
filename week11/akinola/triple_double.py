def TripleDouble(num1,num2):
  str1 = str(num1) 
  str2 = str(num2)
  for t in str1:
    if t*3 in str1 and t*2 in str2:
      return 1
  return 0

# keep this function call here 
print TripleDouble(raw_input())