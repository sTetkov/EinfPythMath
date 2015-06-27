def stripCode(code):
    res=""
    for i in range(0,len(code)):
        if "0"<=code[i]<="9":
            res+=code[i]
    return res

def checkDigit(code):
    code=stripCode(code)
    if len(code)!=13:
        return False
    sum=0
    for i in range(0,12):
        if i%2==0:
            sum+=int(code[i])
        else:
            sum+=(int(code[i])*3)
    if int(code[12])==(10-(sum%10)):
        return True
    return False

def generateCheckDigit(code):
    code=stripCode(code)
    if len(code)!=12:
        return -1
    sum=0
    for i in range(0,12):
        if i%2==0:
            sum+=int(code[i])
        else:
            sum+=(int(code[i])*3)
    return 10-(sum%10)

option=1
while option!=3:
    print("Pleae choose one of the following options")
    print(" 1)Check a ISBN-13 code")
    print(" 2)Generate the Check Digit for an ISBN-13 code")
    print(" 3)Exit")
    option=input("Select Option:")
    if option==1:
        code=input("Insert the ISBN code:")
        if checkDigit(code):
            print("The code is correct")
        else:
            print("The code is faulty")
    elif option==2:
        code=input("Insert the ISBN code:")
        checkDigit=generateCheckDigit(code)
        answer=""
        if checkDigit>=0:
            answer="The checkdigit is "+str(checkDigit)
        else:
            answer="Faulty code"
        print(answer)
    elif option!=3:
        print("Please choose option 1, 2 or 3")