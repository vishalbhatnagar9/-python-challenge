import csv

# Load dataset from budget_data.CSV file
file_path = r"Module 3\Challenge\PyBank\Resources\budget_data.csv"  
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Define Analysis Variables 
total_months = len(data)
net_total = 0
avg_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Calculate Total and Profit/Losses
for i in range(total_months):
    profit_loss = int(data[i]["Profit/Losses"])
    net_total += profit_loss

    if i > 0:
        change = profit_loss - int(data[i - 1]["Profit/Losses"])
        avg_change += change

        # Update greatest increase and decrease
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = data[i]["Date"]
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = data[i]["Date"]

# Calculate Average Change
avg_change /= (total_months - 1)

# Print Analysis to test if code is working on Visual Studio. Please note: The following is commented out to keep code clean. Output is written directly to txt file. 
# print("Financial Analysis")
# print("----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${net_total}")
# print(f"Average Change: ${average_change:.2f}")
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


