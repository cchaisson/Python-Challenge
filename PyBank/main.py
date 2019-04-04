#Import the os module
import os
#Module for reading CSV files
import csv
csvpath = os.path.join('..','budget_data.csv')
#Lists to store data
months=[]
profit_loss=[]
profit_gain=[]
total=0
month_change=[]
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
#Read through each row of data after the header
#Calculate the average of the changes in Profit/Losses over period    
    for row in csvreader:
        destring_value=int(row[1])
        months.append(row[0])
        month_change.append(row[0])
        total=total + destring_value
#Calculate greatest increase in profit by amount and time
    for row in csvreader:
        destring_value=int(row[2])
        profit_gain.append(row[0])
        return max('budget_data.csv')
        print(profit_gain)
#Calculate greatest decrease by amount in profit and time
    for row in csvreader:
        destring_value=int(row[2])
        profit_loss.append(row[0])
        return min('budget_data.csv')
        print(profit_loss)
#Final Script should print analysis to terminal
#Write Script that exports results into a text file
#Store the file path associated with the file 
    file='../OSDisk(C:)/Users/Python-Challenge
#Open the file in read mode (r) and store contents in the variable text
    with open(file, 'r') as text:
        print (text)
#Store all of the text inside a variable called "lines"
        lines=text.read()
#Print the contents of the text file
        print(lines)