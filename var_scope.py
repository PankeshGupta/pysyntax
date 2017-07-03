def main():
    sharedvar = "I am shareable"
    def first():
        print(sharedvar)
        firstvar = "Not shared"
        return
    def second():
        print(sharedvar)
        sharedvar = "hello not shared"
        print(sharedvar)
    
    
if __name__ = "__main__":
    main()

# So def second():
#        print(sharedvar)
#        sharedvar = "hello not shared"
#        print(sharedvar)
# This throws a "UnboundLocalError: local variable 'sharedvar' referenced before assignment
