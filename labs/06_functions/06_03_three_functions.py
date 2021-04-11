'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def hello():
    print("Hello, World!")

    def bye():
        print('Bye World!')
    bye()


def main():
    print("This is the main function.")
    hello()


main()
