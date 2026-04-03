def main():
    number= int(input("Enter a number: "))
    print(positive_or_not(number))

def positive_or_not(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "Not positive"
    else:
        return "Nummber is zero"
    
main()    
