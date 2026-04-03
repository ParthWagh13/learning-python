def main():
    number = int(input("Enter a number: "))
    print(multiple_of_5(number))

def multiple_of_5(number):
    if number % 5 == 0:
        return "Multiple of 5"

    else:
        return "Not a multiple of 5"
main()        