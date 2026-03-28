def main():
    text = input("Enter a sentence: ")
    print(words(text))

def words(text):
    return len(text.split())

main()
