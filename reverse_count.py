def main():
    print("It is a program to print the reverse count using the for loop")
    p = int(input(" please enter the number > 0  "))
    # the input entered is always string therefore convert to an int
    for i in range(p,0,-1):
        print(i)

if __name__ == "__main__":
    main()
