Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = "pankesh"
>>> print("hello {}",format(s))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print("hello {}",format(s))
NameError: name 's' is not defined
>>> print("hello {}",format(name))
hello {} pankesh
>>> print("hello {0}",format(name))
hello {0} pankesh
>>> print("hello {}".format(name))
hello pankesh
>>> print("hello {}".format(name))
hello pankesh
>>> #precision.py
>>> print("{}".format(1/10))
0.1
>>> print("{:.55f}".format(1/10))
0.1000000000000000055511151231257827021181583404541015625
>>> len(print("{:.55f}".format(1/10)))
0.1000000000000000055511151231257827021181583404541015625
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    len(print("{:.55f}".format(1/10)))
TypeError: object of type 'NoneType' has no len()
>>> #:.55f gives us the precision till 55 decimal places
>>> # here we only do 1/10 ,python has actually fixed this , it always gives the float
>>> print("x is ",end = "")
x is 
>>> print("x is ",end = "")
x is 
>>> # python by default give a \n so if we want to bypass it we pass an argument to the print function such as  , end= ""
>>> print("x is ",end= ""0)
SyntaxError: invalid syntax
>>> print("x is ",end= "")
x is 
>>> print("x is ",end= "")
x is 
>>> f= float(input("please enter the temprature"))
please enter the temprature 12.50
>>> f
12.5
>>> #logical in python . funvtion to test logics
>>> c= input("give char")
give chary
>>> if c=='Y' or c=='y':
	print("yes u are allowed")

	
yes u are allowed
>>> if c=='Y' or c=='y':
	print("yes u are allowed")
    elif c=="n" or c=="N"
    
SyntaxError: unindent does not match any outer indentation level
>>> if c=='Y' or c=='y':
	print("yes u are allowed")
    elif c=="n" or c=="N":
	    
SyntaxError: unindent does not match any outer indentation level
>>> if c=='Y' or c=='y':
	print("yes u are allowed")
     elif c=="n" or c=="N":
	     
SyntaxError: unindent does not match any outer indentation level
>>> def allow(s):
	if s=="y" or s=='Y'
	
SyntaxError: invalid syntax
>>> def allow(s):
	if s=="y" or s=='Y' :
		print("yes")
	elif s=="n" or s=="N":
		print("No")
	else:
		print("wrong input")

		
>>> allow(""helo)
SyntaxError: invalid syntax
>>> allow("")
wrong input
>>> # main is not defined y default in python
>>> # if __name__ == "__main__":
>>> # main()
>>> 
========= RESTART: C:/Users/Pankesh/Desktop/py coed/cs50 positive.py =========
>>> 
========= RESTART: C:/Users/Pankesh/Desktop/py coed/cs50 positive.py =========
>>> 
============= RESTART: C:/Users/Pankesh/Desktop/py coed/main.py =============
cough
cough
cough
>>> 
============= RESTART: C:/Users/Pankesh/Desktop/py coed/main.py =============
cough
cough
cough
aacho
aacho
aacho
>>> 
============ RESTART: C:/Users/Pankesh/Desktop/py coed/strlen.py ============
olease enterfdgdfsd
7
>>> 
============ RESTART: C:/Users/Pankesh/Desktop/py coed/strlen.py ============
A is 65
B is 66
C is 67
D is 68
E is 69
F is 70
G is 71
H is 72
I is 73
J is 74
K is 75
L is 76
M is 77
N is 78
O is 79
P is 80
Q is 81
R is 82
S is 83
T is 84
U is 85
V is 86
W is 87
X is 88
Y is 89
Z is 90
>>> 
============ RESTART: C:/Users/Pankesh/Desktop/py coed/sysargv.py ============
bhai galat argument de ra h
>>> 
============= RESTART: C:/Users/Pankesh/Desktop/py coed/argv1.py =============
C:/Users/Pankesh/Desktop/py coed/argv1.py
>>> 
============ RESTART: C:/Users/Pankesh/Desktop/py coed/string.py ============
s:pankeh
s : pankeh
t : <built-in method capitalize of str object at 0x02D3D460>
>>> 
============ RESTART: C:/Users/Pankesh/Desktop/py coed/string.py ============
s:345pa
s : 345pa
t : 345pa
>>> 
============ RESTART: C:/Users/Pankesh/Desktop/py coed/string.py ============
s:panekaah
s : panekaah
t : Panekaah
>>> 
