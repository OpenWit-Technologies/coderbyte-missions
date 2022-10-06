def StringScramble(str1,str2):

  # code goes here
  list1= list(str1)
  list2= list(str2)
  for i in list2:
    if i in list1:
      list1.remove(i)
    else:
      return "false"

  return "true"

# keep this function call here 
print(StringScramble("girl and boy", "boyagirl"))