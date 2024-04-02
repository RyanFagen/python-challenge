import csv
bank_file_path = "PyBank\Resources\money_data.csv"
total_months = 0
net_total = 0
current_value = 0
max_increase = 0
max_decrease = 0
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
print(f'{total_months}')
print(f'{net_total}')
print(f'{max_month}')
print(f'{max_increase}')
print(f'{min_month}')
print(f'{max_decrease}')