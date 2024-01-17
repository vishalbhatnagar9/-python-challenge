PyBank Challenge

Problem Statement:
Create Python script to analyze financial records from data given in budget_data.csv.  The following needs to be deduced by the code from the data provided:
From Module Challenge:
•	The total number of months included in the dataset
•	The net total amount of "Profit/Losses" over the entire period
•	The changes in "Profit/Losses" over the entire period, and then the average of those changes
•	The greatest increase in profits (date and amount) over the entire period
•	The greatest decrease in profits (date and amount) over the entire period

Explanation of code step-by-step:
1.	Import pandas as pd  – importing pandas library and assigning pd as a variable
2.	Loading the data set from budget_data.csv by assigning file path and reading the budget_data.csv file through that file path
     `file_path = r"Module 3\Challenge\PyBank\Resources\budget_data.csv"
      data = pd.read_csv(file_path)`
