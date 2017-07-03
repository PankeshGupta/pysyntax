def main():
    x = 1
    y = 2
    print("x is ",x)
    print("y is ",y)
    # we dont have pointers in python
    swap(x,y)
    print("the new value pf x is ",x)
    print("the new value pf y is ",y)

def swap(a,b):
    tmp = a
    a = b
    b = temp
if __name__ == "__main__":
    main()
    
    
