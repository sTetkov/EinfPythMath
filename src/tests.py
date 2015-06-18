def keller(string,char):
	return string+char

def entkellern(string):
	char=string[len(string)-1]
	x=len(string)-1
	string=string[0:x]
	return (char,string)
	
string='abcd'
string=keller(string,"r")
char=entkellern(string)
print(char[0])
print(char[1])

(x,z)=entkellern(char[1])
print(x)
print(z)