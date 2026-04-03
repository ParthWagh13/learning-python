def main():
    hello()
    name = input ("What is your name? ")
    hello(name)
    morning(name)


#Define a function called hello
def hello(to="World"):
    print ("hello,", to)

#Define a function called morning
def morning(to):
    print ("morning,", to)    

main() 
