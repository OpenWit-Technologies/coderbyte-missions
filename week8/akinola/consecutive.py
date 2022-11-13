def Consecutive(arr):
  l = range(min(arr),max(arr)+1)

  # code goes here
  return len(l)-len(arr)

# keep this function call here 
print Consecutive(raw_input())