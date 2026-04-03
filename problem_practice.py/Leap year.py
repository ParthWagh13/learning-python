def main():
    year = int(input("Ask the user for the year: "))
    print(leap_year_or_not(year))

def leap_year_or_not(year):
    if year % 400 == 0:
        return "Leap year"
    elif year % 100 ==0:
        return "Not a leap year"
    elif year % 4 == 0:
        return "Leap year"
    else:
        return "Not a leap year"

    
main()    