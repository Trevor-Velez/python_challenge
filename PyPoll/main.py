import csv

datafile = 'Resources/election_data.csv'

with open(datafile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    sumVotes = 0
    khanVotes = 0
    correyVotes = 0
    liVotes = 0
    tooleyVotes = 0
    khanPercent = 0
    correyPercent = 0
    liPercent = 0
    tooleyPercent = 0

    for row in csvreader:
        sumVotes += 1
        if row[2] == "Khan":
            khanVotes += 1
        elif row[2] == "Correy":
            correyVotes += 1
        elif row[2] == "Li":
            liVotes += 1
        elif row[2] == "O'Tooley":
            tooleyVotes += 1
        
    khanPercent = (khanVotes / sumVotes) * 100
    correyPercent = (correyVotes / sumVotes) * 100
    liPercent = (liVotes / sumVotes) * 100
    tooleyPercent = (tooleyVotes / sumVotes) * 100

votesList = [khanVotes, correyVotes, liVotes, tooleyVotes]
winnerVotes = max(votesList)
winnerIndex = votesList.index(winnerVotes)
winner = ""

if winnerIndex == 0:
    winner = "Khan"
elif winnerIndex == 1:
    winner = "Correy"
elif winnerIndex == 2:
    winner = "Li"
elif winnerIndex == 3:
    winner = "O'Tooley"


print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {sumVotes}')
print(f'-------------------------')
print(f'Khan: {round(khanPercent, 3)}% ({khanVotes})')
print(f'Correy: {round(correyPercent, 3)}% ({correyVotes})')
print(f'Li: {round(liPercent, 3)}% ({liVotes})')
print(f"O'Tooley: {round(tooleyPercent, 3)}% ({tooleyVotes})")
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')


output_path = 'Analysis/output.txt'

with open(output_path, 'w') as textfile:

    textfile.write(f'Election Results\n')
    textfile.write(f'-------------------------\n')
    textfile.write(f'Total Votes: {sumVotes}\n')
    textfile.write(f'-------------------------\n')
    textfile.write(f'Khan: {round(khanPercent, 3)}% ({khanVotes})\n')
    textfile.write(f'Correy: {round(correyPercent, 3)}% ({correyVotes})\n')
    textfile.write(f'Li: {round(liPercent, 3)}% ({liVotes})\n')
    textfile.write(f"O'Tooley: {round(tooleyPercent, 3)}% ({tooleyVotes})\n")
    textfile.write(f'-------------------------\n')
    textfile.write(f'Winner: {winner}\n')
    textfile.write(f'-------------------------\n')
