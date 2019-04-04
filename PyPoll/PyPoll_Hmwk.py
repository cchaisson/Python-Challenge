#Import the os module
import os
#Module for reading CSV files
import csv
csvpath = os.path.join('..','election_data.csv')
#Lists to store data
candidate=[]
total=0
khan=0
correy=0
li=0
otooley=0

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
#Read through each row of data after the header
    for row in csvreader:
        total+=1
        if row[2]=="Khan":
            khan+=1
        elif row[2]=="Correy":
            correy+=1
        if row[2]=="Li":
            li+=1
        elif row[2]=="O'Tooley":
            otooley+=1    
khanprop = round(khan/total*100, 0)
correyprop = round(correy/total*100, 0)
liprop = round(li/total*100, 0)
otooleyprop = round(otooley/total*100, 0)
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
cand_props=[khan,correy,li,otooley]
zipper=[(k,r) for k, r in zip(candidates, cand_props)]
winner=[k for k,r in zipper if r==max(cand_props)]

#Write Script that exports results into a text file
print("Election Results")
print("-------------------")
print("Total Votes: "+str(total))
print("Khan: "+str(khanprop)+"%"+"    "+str(khan))
print("Corry: "+str(correyprop)+"%"+"    "+str(correy))
print("Li: "+str(liprop)+"%"+"    "+str(li))
print("O'Tooley: "+str(otooleyprop)+"%"+"    "+str(otooley))
print("Winner "+str(winner))