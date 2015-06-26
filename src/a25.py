freeRegs="0123456789"

def gewicht(char):
	if char=="(":
		return 0
	elif char==")" or char ==";":
		return 1
	elif char=="+" or char =="-":
		return 2
	elif char=="*" or char =="/":
		return 3
	elif char=="^":
		return 4
		
def entkellern(string):
	if len(string)==0:
		return("",string)
	char=string[len(string)-1]
	x=len(string)-1
	string=string[0:x]
	return (char,string)
	
def toPostFix(string):
	result=''
	keller=''
	for i in range(0,len(string),1):
		char=string[i]
		if "a"<=char<="z":
			result+=char
		elif char=="(":
			keller+=char
		else:
			(aux,keller)=entkellern(keller)
			while gewicht(aux)>=gewicht(char):
				result+=aux
				(aux,keller)=entkellern(keller)
			if(aux!="&") and (not((aux=="(") and (aux==")"))):
				keller+=aux
			if char!=")":
				keller+=char
	(aux,keller)=entkellern(keller)
	while aux!="":
		if aux!="(":
			result+=aux
		(aux,keller)=entkellern(keller)
	result+=";"
	return result

def setFreeRegs(expr):
	global freeRegs
	freeRegs="0123456789"
	for i in range(0,len(expr)):
		if "0"<=expr[i]<="9":
			j=int(expr[i])
			freeRegs=freeRegs[0:j]+"_"+freeRegs[j+1:len(freeRegs)]

def getFreeReg():
	global freeRegs
	for i in range(0,len(freeRegs)):
		if freeRegs[i]!="_":
			freeRegs=freeRegs[0:i]+"_"+freeRegs[i+1:len(freeRegs)]
			return str(i)
	return "#"
	
def assingRegs(expr):
	instr=""
	if not("0"<=expr[0]<="9"):
		freeReg=getFreeReg()
		instr+="MOVE "+expr[0]+", D"+freeReg+"\n"
		expr=freeReg+expr[1:len(expr)]
	if not("0"<=expr[1]<="9"):
		freeReg=getFreeReg()
		instr+="MOVE "+expr[1]+", D"+freeReg+"\n"
		expr=expr[0]+freeReg+expr[2]
	return (instr,expr)
		
def getRegName(char):
	return "D"+char

def getAssemblyCmd(pfexpr):
	if len(pfexpr)<3:
		return ("","")
	setFreeRegs(pfexpr)
	instr=""
	movInstr=""
	(head,expr,tail)=dismantleExpression(pfexpr)
	(movInstr,expr)=assingRegs(expr)
	instr+=movInstr
	reg1=getRegName(expr[0])
	reg2=getRegName(expr[1])
	
	if expr[2]=="+":
		instr+="ADD "+reg2+", "+reg1+"\n"
	elif expr[2]=="-":
		instr+="SUB "+reg2+", "+reg1+"\n"				
	elif expr[2]=="*":
		instr+="MUL "+reg2+", "+reg1+"\n"			
	elif expr[2]=="/":
		instr+="DIV "+reg2+", "+reg1+"\n"
	elif expr[2]=="^":
		instr+="POT "+reg2+", "+reg1+"\n"
	retVal=head+expr[0]+tail
	return (instr,retVal)
	
def dismantleExpression(expr):
	head=0
	tail=0
	headExpr=""
	tailExpr=""
	toSolve=""
	for i in range(0,len(expr)):
		if (not("a"<=expr[i]<="z") and not("0"<=expr[i]<="9")):
				head=i-1
				tail=i+1
				break
	if head>1:
		headExpr=expr[0:head-1]
	if tail<len(expr):
		tailExpr=expr[tail:len(expr)]
	toSolve=expr[head-1:tail]
	return (headExpr,toSolve,tailExpr)

expr=input("Ausdruck eingeben:")
postFixExpr=toPostFix(expr)
print(postFixExpr)
instructions=""
while postFixExpr!="":
	(aux,postFixExpr)=getAssemblyCmd(postFixExpr)
	instructions+=aux
print(instructions)
