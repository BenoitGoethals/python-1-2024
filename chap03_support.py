#Support program to chap03_func

def add(x, y):
    a = x + y

    #print(a)
    return a

assert add(2, 3) == 5          #will generate an error when you'd make a mistake in your function for example * instead of +

def main():                         #Good practice!!!
    print(add(2 , 3))


if __name__ == '__main__':          #only run this code when you're really running the file
    main()                          #Good practice!!!
