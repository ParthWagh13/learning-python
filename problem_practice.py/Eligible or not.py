def main():
    age = int(input("Enter your age: "))
    print(Eligible_ornot(age))

def Eligible_ornot(x):
    if x >= 18:
        return "Eligible"
    else:
        return "Not eligible"

main()