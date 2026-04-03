def main():
    x =int(input("Enter a number: "))
    y =int(input("Enter a number: "))
    z =int(input("Enter a number: "))
    print(largest_of_3(x,y,z))

def largest_of_3(x,y,z):
    if x > y and x > z:
        return "The first number is the largest"
    elif y > x and y > z:
        return "The second number is the largest"
    elif z> x and z > y:
        return "The third number is the largest"
    elif x == y and x > z:
        return "The first and second number are the largest"
    elif x == y and z > x:
        return "The third number is the largest"
    elif z == x and x > y:
        return "The first and third number are the largest"
    elif x == z and y > x:
        return "The second number is the largest"
    elif y == z and x > y:
        return "The first number is the largest"
    elif y == z and y > x:
        return "The second and third number is the largest"
    else:
        return "All 3 numbers are equal"
    
main()    