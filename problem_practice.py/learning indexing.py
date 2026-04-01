#Defined a function
def main():
    x = (input("Enter a word: "))
    print(first_letter(x))

#The [] against any variable show the positions of thier characters
def first_letter(x):
    return x[0]

main()