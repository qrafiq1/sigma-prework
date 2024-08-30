from datetime import datetime


def calculateAge(givenDateStr):
    givenDate = datetime.strptime(givenDateStr, "%d-%m-%Y")
    currentDate = datetime.today()
    age = currentDate.year - givenDate.year

    if currentDate.month < givenDate.month:
        age -= 1
    elif (currentDate.month == givenDate.month) & (currentDate.day < givenDate.day):
        age -= 1

    print(age)


date = input("enter a date in the format dd-mm-yyyy: ")

calculateAge(date)
