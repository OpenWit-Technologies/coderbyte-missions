def LetterChanges(strParam):
   
  newString = ""

  
  for char in strParam:
    
    
    if char.isalpha():

     
      if char.lower() == 'z':
        char = 'a'


      else:
        char = chr(ord(char) + 1)


    if char in 'aeiou':
      char = char.upper()


    newString = newString + char

  return newString
  


print LetterChanges(raw_input())