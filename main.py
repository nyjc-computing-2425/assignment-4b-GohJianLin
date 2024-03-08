stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
valid = ["1","2","3",'4','5','6','7','8','9','0',"E","x",".","-","^"]
k = stdform.find("^") 
digit = 0
for i in range(len(stdform)):
  if str(stdform)[i] not in valid:
    digit += 1
if digit == 0 and stdform.count(".") == 1 and stdform[k+1:].isdigit:
  print(f"This number in E notation is {stdform.replace('x10^','E')}.")
else: 
  print("Error converting to scientific E notation.")