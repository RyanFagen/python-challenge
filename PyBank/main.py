import csv
bank_file_path = "PyBank\Resources\money_data.csv"
total_months = 0
net_total = 0
current_value = 0
previous_value = 0
max_increase = 0
max_decrease = 0
changes = []
monthly_change = 0
average_change = 0
max_month = "null"
min_month = "null"
with open(bank_file_path) as bank_file:
    csv_file = csv.reader(bank_file)
    next(csv_file)
    for row in csv_file:
        total_months += 1
        current_value = int(row[1])
        net_total += int(row[1])
        if (current_value > max_increase):
            max_month = row[0]
            max_increase = current_value
        elif (current_value < max_decrease):
            min_month = row[0]
            max_decrease = current_value
        if (total_months > 1):
            monthly_change = current_value - previous_value
            changes.append(monthly_change)
        previous_value = current_value
average_change = sum(changes) / len(changes)
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {max_month} (${max_increase})')
print(f'Greatest Decrease in Profits: {min_month} (${max_decrease})')
out_file_path = "PyPoll\election_results.txt"
with open(out_file_path, 'w') as file_out:
    file_out.write("Financial Analysis\n")
    file_out.write("----------------------------\n")
    file_out.write(f'Total Months: {total_months}\n')
    file_out.write(f'Total: ${net_total}\n')
    file_out.write(f'Average Change: ${average_change:.2f}\n')
    file_out.write(f'Greatest Increase in Profits: {max_month} (${max_increase})\n')
    file_out.write(f'Greatest Decrease in Profits: {min_month} (${max_decrease})\n')