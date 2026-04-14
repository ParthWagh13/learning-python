#Made the value and count 0
value = 0
count = 0
x = int(input("Enter a positive integer: "))
while x >= 0:
    value = value + x
    count = count +1 #This is a loop calculator which tells how many times loop has been executed
    x = int(input("Enter a positive integer: "))    
if count == 0:
    print("No values entered")
else:
    average = value / count

print(f"The average is {average}")
