#Define a main function
def main():
    x = int(input("Enter a number: "))
    print(f"The square of the number is {square(x)}")

#Define another function which multiplies the number to itself
def square(x):
    return x * x

main()    