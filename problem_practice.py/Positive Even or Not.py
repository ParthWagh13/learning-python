def main():
    number = int(input("Enter a number: "))
    print(positive_even_or_not(number))

def positive_even_or_not(number):
    if number > 0 and number % 2 == 0:
        return "Positive Even Number"
    else:
        return "Not a positive even number"

main()       