# this method of cresting list is called as list comprehensions
# in this method we write list with the help of for loop

def main():
    squares = []
    squares = [i*i for i in range(0,11)]
    # This expression will insert the first 10 squares inside the list
    # here was a very simple example of writting it
    # here is the general syntax for it
    #[*expression* for *element* in *range* if *condition*]

    even_square = [i*i for i in range(1,11) if i%2==0 ]

    print("The squares of 1st 10 natural no. is  {} ".format(squares) )
    print("==========================================================")
    print("The square of even natural no. is  {} ".format(even_square ))
if __name__ == "__main__" :
    main()
