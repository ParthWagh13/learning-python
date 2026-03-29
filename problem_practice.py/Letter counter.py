def main():
    text = input("Enter a word: ")
    print(f"The number of letters is {letter_counter(text)}")

def letter_counter(text):
    return len(text)

main()
