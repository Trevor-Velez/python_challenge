import os
import csv

datafile = 'Resources/budget_data.csv'

with open(datafile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    count = 0
    sumofPL = 0
    maxList = []
    changes = 0
    previousPL = 0
    
    for row in csvreader:
        count += 1
        sumofPL += int(row[1])
        maxList.append(int(row[1]))

        changes += (int(row[1]) - previousPL)
        previousPL = int(row[1])


        
    maxProfit = max(maxList)
    maxLoss = min(maxList)
    maxProfitMonth = ""
    maxLossMonth = ""
    averageChange = changes / count
    
with open(datafile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)   
    
    for row in csvreader:
        if int(row[1]) == maxProfit:
            maxProfitMonth = row[0]
        elif int(row[1]) == maxLoss:
            maxLossMonth = row[0]
            

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {count}')
print(f'Total: {sumofPL}')
print(f'Average Change: ${round(averageChange, 2)}')
print(f'Greatest Increase in Profits: {maxProfitMonth} (${maxProfit})')
print(f'Greatest Decrease in Profits: {maxLossMonth} (${maxLoss})')

output_path = 'Analysis/output.txt'

with open(output_path, 'w') as textfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile)

    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f'Total Months: {count}\n')
    textfile.write(f'Total: {sumofPL}\n')
    textfile.write(f'Average Change: ${round(averageChange, 2)}\n')
    textfile.write(f'Greatest Increase in Profits: {maxProfitMonth} (${maxProfit})\n')
    textfile.write(f'Greatest Decrease in Profits: {maxLossMonth} (${maxLoss})\n')