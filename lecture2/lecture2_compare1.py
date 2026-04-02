x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if x > y:
    print("x is greater than y")
#elif basically prevents your computer from executing unnecessary code, i.e if the first statement is already true the code wont execute this
elif x < y:
    print("y is greater than x")

else:
    print("x is equal to y")        