# Questions Marks

#Have the function QuestionsMarks(str) take the str string parameter, 
# which will contain single digit numbers, letters, and question marks, 
# and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

# Questions Marks

#Have the function QuestionsMarks(str) take the str string parameter, 
# which will contain single digit numbers, letters, and question marks, 
# and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

def QuestionsMarks(strParam):
    
  # check if there are exactly 3 question marks between every pair of two numbers that add up to 10
  for i in strParam:
    if i.isdigit() and int(i) + int(strParam[strParam.index(i) + 2]) == 10:
      if strParam[strParam.index(i) + 1] != '?':
          return 'false'
      elif strParam[strParam.index(i) + 3] != '?':
          return 'false'
      elif strParam[strParam.index(i) + 4] != '?':
          return 'false'
      else:
          return 'true'
  return strParam

# keep this function call here 
# print QuestionsMarks(raw_input())

# keep this function call here 
# print (QuestionsMarks(raw_input()))

if __name__ =='__main__':
    
    raw_input = "Akinola is a software developer, isn't he????"
    print(QuestionsMarks(raw_input))