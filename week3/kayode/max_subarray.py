def MaxSubarray(arr):
  # code goes here
  temp1 = 0
  for i in range(len(arr)):
    temp2 = arr[i]
    for j in range(i+1, len(arr)):
      temp3 = sum(arr[i:j])
      if temp3 > temp2:
        temp2 = temp3
    
    if temp2 > temp1:
      temp1 = temp2

  return temp1

# keep this function call here 
# print(MaxSubarray(input()))

if __name__ == "__main__":
    print(MaxSubarray([1, -2, 0, 3]))