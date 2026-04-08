def main():
    x = int(input("Enter a Positive Number: "))
    number(x)

def number(y):
    while y <= 0:
        y = int(input("Enter a Positive Number: "))

main()              