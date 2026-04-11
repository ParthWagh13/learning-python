#Define a mian function
def main():
    x = int(input("Enter a positive integer: "))
    while x != 1:
        #Call if and else before not in function
        if x % 2 == 0:
              x = even(x)
        else:      
              x = odd(x)
        print(x)

def odd(x):
        return(x * 3 + 1)


def even(x):
        return(x//2)

main()
