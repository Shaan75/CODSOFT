import random
import string
print ("Welcome to our Random Password Generator")
def shaan():
    length=int(input("Enter The length of password: "))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine= lowerD+upperD+digitD+symbolsD
    x= random.sample(combine, length)
    password="".join(x)
    print("PASSWORD: ",password)
    shaan()
shaan()
