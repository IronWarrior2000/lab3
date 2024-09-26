#Bill Nguyen | 9/26/24 | Lab 3
import csv


def fetchData():
    try:
        with open("lab3/budget_data.csv","r") as file:
            fetchData = csv.reader(file)
            next(fetchData)
            data = []
            for values in fetchData:
                data.append(values)
            return data
    except FileNotFoundError: #If the file is not founder
        print("The file was not found.") #It will print out this error
    except ValueError:
        print("An error occurred with the Value.")

def userInput():
    user = input("Enter in the day of the profit")
    return user

def serialData(data, date):
    for value in data:
        if date in value[0]:
            serial = f"{date}:${value[1]}"
            return serial

def searchData():
    data = fetchData()
    print(f"What Date are you looking for?\n")
    for each in data:
        print(each[0])
    date = userInput()
    serial = serialData(data, date)
    print(serial)

def main():
    while True:
        try:
            searchData()
            repeat = input("Would you like to try this again?(Y|N)").upper() #WILL AUTOMATICALLY MAKE EVERY REPLY TO THIS CAPITALIZE
            if repeat != 'Y':   
                break
      #  except ValueError: #Will print an ValueError for an exception
         #   print("ValueError")
        except ZeroDivisionError:  #Will print an ZeroDivisionError for an exception
            print("ZeroDivisionError")     
        
main()