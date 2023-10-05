import os , csv
electioncsv = os.path.join('/Users/j.mai.le/python_challenge/PyPoll/Resources/election_data.csv')
totalvote= 0
vote = []
charles = 0
diana = 0
raymon = 0
with open(electioncsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    date = next(csvreader)
    first = next(csvreader)
    totalvote = totalvote + 1
    for row in csvreader:
        totalvote = totalvote + 1
    
        candidate = row[2] 
        if (candidate == "Charles Casper Stockham" ):
            charles = (charles + 1)
            charles1 = charles +1
        elif (candidate == "Diana DeGette"):
            diana = (diana + 1)
        elif (candidate == "Raymon Anthony Doane"):
            raymon = (raymon + 1)
            
        
print('Election Results')
print('----------------------------')
print(f'Total Votes :  {totalvote}')
print('----------------------------')
print(f'Charles Casper Stockham: {charles1*100/totalvote:.3f} % ({charles1}) ')
print(f'Diana DeGette: {diana*100/totalvote:.3f} % ({diana})')
print(f'Raymon Anthony Doane: {raymon*100/totalvote:.3f} % ({raymon}) ')
print('----------------------------')
print(f' Winner: Diana DeGette')
print('----------------------------')