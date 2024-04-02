import csv
bank_file_path = "PyPoll\Resources\budget_data.csv"
total_months = 0
net_total = 0
max_increase = 0
min_increase = 0
max_month = "null"
min_month = "null"
with open(bank_file_path) as bank_file:
    csv_file = csv.reader(bank_file)
    next(csv_file)