def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Enter text: ")
    result = convert(user_input)
    print(result)

# Call main
if __name__ == "__main__":
    main()