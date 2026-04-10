def main():
        x = int(input("Guess the number: "))
        while x != 6:
               higher_or_lower(x)
               x = int(input("Guess the number: "))  
        print("Correct")

def higher_or_lower(x):
    if x > 6:
            print("Lower")
    elif x < 6:
            print("Higher")

main()              