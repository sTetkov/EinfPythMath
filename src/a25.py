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
	print(freeRegs)

def getFreeReg():
	global freeRegs
	for i in range(0,len(freeRegs)):
		if freeRegs[i]!="_":
			freeRegs=freeRegs[0:i]+"_"+freeRegs[i+1:len(freeRegs)]
			return str(i)
	return "#"
	
def assingRegs(expr,i):
	instr=""
	if not("0"<=expr[i-2]<="9"):
		freeReg=getFreeReg()
		instr+="MOVE "+expr[i-2]+", D"+freeReg+"\n"
		expr=expr[0:i-3]+freeReg+expr[i-1:len(expr)]
	if not("0"<=expr[i-1]<="9"):
		freeReg=getFreeReg()
		instr+="MOVE "+expr[i-1]+", D"+freeReg+"\n"
		expr=expr[0:i-2]+freeReg+expr[i:len(expr)]
	return (instr,expr)
		
def getRegName(char):
	return "D"+char

def getAssemblyCmd(expr):
	setFreeRegs(expr)
	instr=""
	reg1=""
	movInstr=""
	for i in range(0,len(expr)):
		if not("a"<=expr[i]<="z"):
			(movInstr,expr)=assingRegs(expr,i)
			instr+=movInstr
			print (expr)
			if expr[i]=="+":
				reg1=getRegName(expr[i-2])
				reg2=getRegName(expr[i-1])
				instr+="ADD "+reg2+", "+reg1+"\n"
			elif expr[i]=="-":
				reg1=getRegName(expr[i-2])
				reg2=getRegName(expr[i-1])
				instr+="SUB "+reg2+", "+reg1+"\n"				
			elif expr[i]=="*":
				reg1=getRegName(expr[i-2])
				reg2=getRegName(expr[i-1])
				instr+="MUL "+reg2+", "+reg1+"\n"			
			elif expr[i]=="/":
				reg1=getRegName(expr[i-2])
				reg2=getRegName(expr[i-1])
				instr+="DIV "+reg2+", "+reg1+"\n"
			else:
				reg1=getRegName(expr[i-2])
				reg2=getRegName(expr[i-1])
				instr+="POT "+reg2+", "+reg1+"\n"
			retVal=""+expr[0:i-2]+reg1+expr[i+1:len(expr)]
			print(retVal)
			return (instr,retVal)
	return("",expr)
	
expr=input("Ausdruck eingeben:")
postFixExpr=toPostFix(expr)
print(postFixExpr)
instructions=""
(aux,postFixExpr)=getAssemblyCmd(postFixExpr)
instructions+=aux
#while postFixExpr!="":
	#(aux,postFixExpr)=getAssemblyCmd(postFixExpr)
	#instructions+=aux
print(instructions)
