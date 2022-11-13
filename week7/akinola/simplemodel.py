def SimpleMode(arr): 
  mode = -1
  count = 1
  for i in arr:
    if arr.count(i)> count:
      count = arr.count(i)
      mode = i
 

  # code goes here
  return mode

# keep this function call here 
print SimpleMode(raw_input())