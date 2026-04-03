#Define a main function
def main():
    number= int(input("Enter a number: "))
    print(positive_or_not(number))

#Define another function make sure to use elif and else
def positive_or_not(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "Not positive"
    else:
        return "Nummber is zero"
    
main()    
