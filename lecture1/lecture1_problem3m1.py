#Ask user for mass and make 'c' a constant also remember to define 'm' and 'c' in 'E'
def main():
    m = int(input("What is the required m? "))
    c = 300000000
    print("E:", E(m,c))
#Define E as a function
def E(m,c):
    return m * c * c

main()