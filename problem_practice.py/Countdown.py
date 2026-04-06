def main():
    count = int(input("Enter a number: "))
    countdown(count)

def countdown(x):
    while x >= 1:
        print(x)
        x = x - 1    

main()    