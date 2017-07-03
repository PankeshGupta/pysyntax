import sys
# sys is a system module it has many low level functinalities
# command line arguments, if the no. of command line argument is 2 then i will print the econd one because teh firt will be the name of the progam
if len(sys.argv)==2:
    print("hello, {}".format(sys.argv[1]))
else:
    print("bhai galat argument de ra h")
    
