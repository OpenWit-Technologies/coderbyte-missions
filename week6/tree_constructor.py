def TreeConstructor(strArr):
  parent={}
  for i in range(len(strArr)):
      if strArr[i][1] not in parent:
          parent[strArr[i][2]]=1
      else:
          parent[strArr[i][2]]+=1
          if parent[strArr[i][2]] >2:
              return False
  return True
  # code goes here
  return strArr

# keep this function call here 
print TreeConstructor(raw_input())