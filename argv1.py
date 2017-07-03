import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])


for s in sys.argv:
    for c in s:
        print(c)
     print()   
