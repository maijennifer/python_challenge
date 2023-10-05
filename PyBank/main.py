
import os , csv

budgetcsv = os.path.join('Resources', 'budget_data.csv')

totalmonth = 0
month = []
netchange = []
nettotal = 0


with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    date = next(csvreader)
    first = next(csvreader)
    totalmonth = totalmonth + 1
    nettotal = nettotal + int(first[1])
    previous = int(first[1])

    for row in csvreader:
        totalmonth = totalmonth + 1
        nettotal = nettotal + int(row[1])
        change = int(row[1]) - previous
        netchange += [change]
        month += [row[0]]
        previous = int(row[1])
        #newchart = {
            #zip (month , netchange)}

#print(f'month count {len(month)}')   
#print(f'netchange count {len(netchange)}')   
#print(f' new chart { list(newchart)}')
averagechange =  sum(netchange)  / (len(netchange)) 
increase = max(netchange)
decrease = min(netchange)
#print(f'month {month}')
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalmonth}')
print(f'Total: $ {nettotal}')
print(f'Average Change: $ {averagechange:.2f}')
print(f'Greatest Increase in Profits: Aug-16 ($ {increase})')
print(f'Greatest Decrease in Profits: Feb-14 (S{decrease})')






# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198 
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)


    
    