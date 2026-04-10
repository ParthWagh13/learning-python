def main():
        x = int(input("Guess the number"))
        higher_or_lower(x)
        secret_number(x)

def higher_or_lower(x):
    if x > 6:
            print("Lower")
    elif x < 6:
            print("Higher")

def secret_number(x):
       while x != 6:
              x = int(input("Guess the number"))

main()              