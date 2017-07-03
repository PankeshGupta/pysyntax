def main():
    name = input("Please enter a valid name: ")
    if name and name.isalpha():
        print("The name entered is valid ")
    else:
        print("The name is not valid ")

if __name__ == "__main__" :
    main()
    
