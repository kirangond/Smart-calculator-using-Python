responses=["welcome to smart calculator","My name is munna","thanks",
           "sorry this is beyond my ability"]  #list of strings
def extract_numbers_from_text(text):  #function with text argument
    l=[]
    for t in text.split(' '): #on the basis of split
       try:
           l.append(float(t)) #exception for string
       except valueError:
           pass    #pass nothing
    return 1

def lcm(a,b):             #L.C.M function
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1

def hcf(a,b):            #H.C.F function
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
def add(a,b):      #add function
    return a+b
def sub(a,b):      #subtract function
    return a-b
def multiply(a,b):  #multiply function
    return a*b
def divide(a,b):  #division function
    return (a/b)
def modulus(a,b):   #modulus function
    return a%b;
def end():   #to terminate program
  print(responses[2])
  input("press enter key to exit")
  exit()

def myname():  #print name function
    print(responses[1])

def sorry():  #print beyond my ability
    print(responses[3])
"""
using dictionary we can match
key with different values and  value pair with function
"""
operations={"PLUS":add,"ADDITION":add,"SUM":add,"ADD":add,
            "SUBTRACT":sub,"MINUS":sub,"DIFFRENCE":sub,"SUB":sub,
            "PRODUCT":multiply, "MULTIPLICATION":multiply,"MULTIPLY":multiply,
            "DIVIDE":divide,"DIVISION":divide,"MOD":modulus,"MODULUS":modulus
            }
commands={"NAME":myname,"QUIT":end,"EXIT":end,"CLOSE":end}
            
