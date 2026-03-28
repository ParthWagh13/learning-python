#Define a main function
def main():
    text = input("Enter a word: ")
    print(long_or_short(text))
#Define a function and remember return function returns the value, no need to add print as we let the main do the printing
def long_or_short(text):
    if len(text) >=5:
        return "long"
    else:
        return "short"
    
main()    