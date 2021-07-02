#!/usr/bin/env python
# coding: utf-8

# In[41]:


import os
import csv


# In[42]:


datafile = 'Resources/budget_data.csv'


# In[43]:


with open(datafile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    count = 0
    sumofPL = 0
    monthList = []
    changes = 0
    previousPL = 0
    changeList = []
    
    for row in csvreader:
        count = count + 1
        sumofPL = sumofPL + int(row[1])
        change = int(row[1]) - previousPL
        changeList.append(change)
        monthList.append(row[0])
        previousPL = int(row[1])


# In[44]:


maxChange = max(changeList)
maxChangeIndex = changeList.index(maxChange)
maxChangeMonth = monthList[maxChangeIndex]

minChange = min(changeList)
minChangeIndex = changeList.index(minChange)
minChangeMonth = monthList[minChangeIndex]


# In[45]:


changeList.pop(0)
averageChange = sum(changeList) / len(changeList)


# In[46]:


print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {count}')
print(f'Total: {sumofPL}')
print(f'Average Change: ${round(averageChange, 2)}')
print(f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange})')
print(f'Greatest Decrease in Profits: {minChangeMonth} (${minChange})')


# In[47]:


output_path = 'Analysis/output.txt'


# In[48]:


with open(output_path, 'w') as textfile:

    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f'Total Months: {count}\n')
    textfile.write(f'Total: {sumofPL}\n')
    textfile.write(f'Average Change: ${round(averageChange, 2)}\n')
    textfile.write(f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange})\n')
    textfile.write(f'Greatest Decrease in Profits: {minChangeMonth} (${minChange})\n')


# In[ ]:




