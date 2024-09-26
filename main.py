#Bill Nguyen | 9/26/24 | Lab 3
import csv #imported the csv library


def fetchData(): #This will fetch the data and store it into a function that is callable anytime
    try:
        with open("lab3/budget_data.csv","r") as file: #opens and read budgetdata.csv file and save it as file
            fetchData = csv.reader(file) #fetchData is reading it as an csv file
            next(fetchData) #Skips header
            data = [] #created an empty lists
            for values in fetchData: #for each value in the fetchData
                data.append(values) #The value will be appended to the data list
            return data #and it will return it
    except FileNotFoundError: #If the file is not founder
        print("The file was not found.") #It will print out this error
    except ValueError: #If a wrong input was in the file
        print("An error occurred with the Value.") #it will print out an error

def userInput(): #this is to gather what date that someone wanted to look up
    user = input("Enter in the day of the profit") #gather the input from user
    return user #return user input

def serialData(data, date): #this searches through the data to find the date to print out the date and value.
    for value in data: #for each value within the data
        if date in value[0]: #if the Date is in the value first column
            serial = f"{date}:${value[1]}" #it will save the date and value in the second column as serial
            return serial #and returns it

def searchData(): #This is a junction function that connects all of the other functions together
    data = fetchData() #fetches the data for distribution

    #These set of code is for displaying what date does the user want to find
    print(f"What Date are you looking for?\n") #it will print out the header
    for each in data: #and for each value in data
        print(each[0]) #it will print out each value first column

    date = userInput() #ask the user what date they want to search up
    serial = serialData(data, date) #Send the data and target date in the serial data
    print(serial) #prints out the serial search data

def main(): 
    while True: #while True
        try:
            searchData() #Will search through the data
            repeat = input("Would you like to try this again?(Y|N)").upper() #WILL AUTOMATICALLY MAKE EVERY REPLY TO THIS CAPITALIZE
            if repeat != 'Y':   
                break
        except ValueError: #Will print an ValueError for an exception
            print("ValueError")
        except ZeroDivisionError:  #Will print an ZeroDivisionError for an exception
            print("ZeroDivisionError")     
        
main()