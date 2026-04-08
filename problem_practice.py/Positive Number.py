#Define a main function
def main():
    x = int(input("Enter a Positive Number: "))
    number(x)

#Define another function and remmeber whenever repeating sums are asked use input command not print
def number(y):
    while y <= 0:
        y = int(input("Enter a Positive Number: "))
    print("Thank You")

main()              