def main():
    count = int(input("Enter a number: "))
    #Do not use print function here
    countdown(count) 

def countdown(x):
    while x >= 1:
        print(x) #Use the print function instead of return as it just returns one final value while print keeps printing
        x = x - 1    

main()    