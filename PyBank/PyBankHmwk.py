#Import the os module
import os
#Module for reading CSV files
import csv
csvpath = os.path.join('.','budget_data.csv')
#Lists to store data
months=[]
profit_current=[]
profit_past=[]
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
#Calculate greatest increase and decrease in profit by amount and time
        destring_value=int(row[1])
        profit_current.append(destring_value)
        profit_past.append(destring_value)
del(profit_current[0])
del(profit_past[len(months)-1])
del(month_change[0])
change_MoM=[k-r for k, r in zip (profit_current, profit_past) ]
change_total_MoM=sum(change_MoM)
change_MoM_list=[(k,r) for k, r in zip(month_change, change_MoM)]
#Calculate Min and Max Date
maxdate=[k for k,r in change_MoM_list if r==max(change_MoM)]
mindate=[k for k,r in change_MoM_list if r==min(change_MoM)]
#Final Script should print analysis to terminal
#Write Script that exports results into a text file
print("Financial Analysis")
print("-------------------")
print("Total Months:  "+str(len(months)))
print("Total: "+"$"+str(total))
print("Average Change: "+"str(round(change_total/(len(months")
print("Greatest Increase in profits: "+str(maxdate)+"$"+str(max(change_MoM)))
print("Greatest Decrease in profits: "+str(mindate) + "$" +str(min(change_MoM)))
#Store the file path associated with the file 
print("Financial Analysis")
print("--------------------")
print("Total Months: "+str(len(months)))
print("Total: "+"$"+str(total))
print("Average Change: "+"$"+str(total))
print("Greatest Increase in profits: "+str(maxdate) + "$" + str(max(change_MoM)))
print("Greatest Decrease in profits: "+str(mindate) + "$" +str(min(change_MoM)))
