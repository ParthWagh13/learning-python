#Define a main function
def main():
    #Create a variable x
    x = int(input("What is your age? "))
    #Print the function
    print(adult_or_minor(x))

#Define a function
def adult_or_minor(age):
    #Make an if/else condition and use return function
    if age >= 18:
        return("Adult")
    else:
        return("Minor")

main()           