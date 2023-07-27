A security analyst is reviewing code for improper input validation.   
 
Which type of input validation does this code show? 
 
isValidNumber = False 
while not isValidNumber: 
try: 
pickedNumber = int(input('Pick a number from 1 to 10')) 
if pickedNumber >= 1 and pickedNumber <= 10: 
 isValidNumber = True 
except: 
print('You must enter a valid number from 1 to 10') 
print('You picked the number ' + str(pickedNumber)) 
 
A. Type and range check  (CORRECT)

B. Type and length check

C. Length and range check

D. Invalid number check
