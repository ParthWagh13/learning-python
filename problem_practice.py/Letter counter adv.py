#Create a main function and use the f string
def main():
    text = input("Enter a word: ")
    print(f"The number of letters is {letter_counter(text)}")

#Defined a function which uses len function
def letter_counter(text):
    return len(text)

main()
