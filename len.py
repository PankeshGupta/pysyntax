def main():
    l = [1,2,3,4,5]
    # so here is a function to demonstrate how len works inside the hood
    dic = {1:'one',2:'two',3:'Three'}
      
    def lendict():
        count = 0
        lin = input("please enter the element of list space seprated \n")
        lseq = lin.split()
        lseq = [ int(i) for i in lseq if i.isnumeric() ]
        
        if type(lseq) in [len,dict]:
            return -1                # when we return -1 it means the consition failed
        else :
            for element in lseq:
                count +=1
        print("The length is {}".format(count))            
    lendict()
    
            
if __name__ == "__main__":
    main()
