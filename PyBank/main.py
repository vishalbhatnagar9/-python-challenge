import pandas as pd

# Load dataset from budget_data.CSV file
file_path = r"Module 3\Challenge\PyBank\Resources\budget_data.csv"
data = pd.read_csv(file_path)

# Define Analysis Variables
total_months = len(data)
net_total = data['Profit/Losses'].sum()
avg_change = data['Profit/Losses'].diff().mean()
greatest_increase = data['Profit/Losses'].diff().max()
greatest_increase_date = data.loc[data['Profit/Losses'].idxmax(), 'Date']
greatest_decrease = data['Profit/Losses'].diff().min()
greatest_decrease_date = data.loc[data['Profit/Losses'].idxmin(), 'Date']

# Print Analysis to test if code is working on Visual Studio. Please note: The following is commented out to keep code clean and output directly to txt file.
# print("Financial Analysis")
# print("----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${net_total}")
# print(f"Average Change: ${avg_change:.2f}")
# print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
# print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Print Analysis to budget_data.txt
output_file_path = r"C:\Users\shrut\OneDrive\Desktop\Bootcamp\Module 3\Challenge\python-challenge\Analysis\budget_data.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${avg_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
