#Defined a main function
def main():
    text = input("Enter a sentence: ")
    print(words(text))
#Created another function which returns the value
def words(text):
    return len(text.split()) #Remember that split function can only be used after a variable

main()
