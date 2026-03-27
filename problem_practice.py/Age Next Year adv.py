#Define a main function 
def main():
    #Make a variable x
    x = int(input("What is your age? "))
    
    #You can also use f string
    print("Your age next year is", age(x))



#Define the function age and put x as default
def age(x):
    return x + 1

main()