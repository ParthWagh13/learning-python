# Ask users for a number
def main():
    x = int(input("Enter a number "))
    print ("the square of number is", square(x) )

#Define a square function you can also use pow comman
def square(n):
    return n * n

main()