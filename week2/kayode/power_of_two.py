def PowersofTwo(num):

  #first check the modulus of the number
  if num % 2 != 0:
    soutput= "false"
  else:
    soutput= "false"
    ftemp= num / 2
    while ftemp % 2 == 0:
      if ftemp == 2:
        soutput= "true"
        break
      ftemp= ftemp/2
      
  
  return soutput

# keep this function call here 
# print(PowersofTwo(input()))

if __name__ == "__main__":
    print(PowersofTwo(4))