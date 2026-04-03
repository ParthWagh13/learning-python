#Define a function
def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(Largest_of_two(x,y))
#Define another function and use basic comparison
def Largest_of_two(x,y):
    if x > y:
        return "The first number is larger"
    elif y > x:
        return "The second number is larger"
    else:
        return "Both numbers are equal"
    
main()    