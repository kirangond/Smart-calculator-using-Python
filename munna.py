import sys #import module
sys.path.append('/mymodules/') #path reference variable inside append function
import mymodules
from mymodules.math import *
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("enter some text")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
               l=extract_numbers_from_text(text)
               r=opertaions[word.upper()](l[0],l[1])
               print(r)
            except:
                print("something is wrong please retry")
            finally:
              break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
       sorry()  
        
            
