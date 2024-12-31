# date = input("Enter date (dd-mm-yyyy): ")

def isLeapYear(year):
    return True if (year%4 == 0 and year%100 != 0) or (year%400 == 0) else False

def validDate(date):
    date = [int(i) for i in date.split("-")] # list as [day, month, year]
    day = date[0] ; month = date[1] ; year = date[2]

    daysInMonth = [31, 29 if isLeapYear(date[2]) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # check year
    if year < 1900 or year > 2050:
        return False
    
    # check day and corresponding month
    if day < 1 or day > daysInMonth[month-1]:
        return False;

    return True

date = "29-02-2044"

yn = validDate(date)

print("Valid" if yn else "Not Valid")