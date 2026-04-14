value = 0
count = 0
x = int(input("Enter a positive integer: "))
while x >= 0:
    value = value + x
    count = count +1
    x = int(input("Enter a positive integer: "))    
if count == 0:
    print("No values entered")
else:
    average = value / count

print(f"The average is {average}")
