#Define a main function
def main():
        x = int(input("Guess the number: "))
#Make the while function inside the main function and keep higher or lower in the loop as the hint needs to be after the guess
        while x != 6:
               higher_or_lower(x)
               x = int(input("Guess the number: "))  
        print("Correct")
#Define a seperate function which will act ass assisting function for main loop
def higher_or_lower(x):
    if x > 6:
            print("Lower")
    elif x < 6:
            print("Higher")

main()              