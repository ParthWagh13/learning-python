#Ask users for age
def main():
    age = int(input("What is your age "))
    print ("Your age in days is" , days(age))

#Define the function and multiple it by 365
def days(n):
    return n * 365
 
main() 
        


