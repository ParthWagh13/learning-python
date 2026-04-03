#Define a main function
def main():
    age = int(input("Enter your age: "))
    print(Eligible_or_not(age))

#Define another function and remember to use qutations after return function
def Eligible_or_not(x):
    if x >= 18:
        return "Eligible"
    else:
        return "Not eligible"

main()