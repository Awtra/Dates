#This program prints the date

#Initialize Variables
date = str(input("Enter date in mm/dd/yy format: "))
day = 0
month = 0
month2 = date[0:2]
year = 0
index = 0

#Create a for loop for the date
for index in range(len(date)):
    day = date[3:5]
    year = date[6:10]
    if month2 == "01":
        month = "January"
    if month2 == "02":
        month = "February"
    if month2 == "03":
        month = "March"
    if month2 == "04":
        month = "April"
    if month2 == "05":
        month = "May"
    if month2 == "06":
        month = "June"
    if month2 == "07":
        month = "July"
    if month2 == "08":
        month = "August"
    if month2 == "09":
        month = "September"
    if month2 == "10":
        month = "October"
    if month2 == "11":
        month = "November"
    if month2 == "12":
        month = "December"

#This is a print statement for the date.
print("The date is :", month, day, year)
