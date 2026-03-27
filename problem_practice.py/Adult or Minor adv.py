def main():
    x = int(input("What is your age? "))
    print("adult_or_minor(x)")

def adult_or_minor(age):
    if age >= 18:
        return("Adult")
    else:
        return("Minor")

main()           