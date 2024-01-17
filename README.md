# Module 3 Challenge
## PyBank Challenge

### Problem Statement:

Create Python script to analyze financial records from data given in budget_data.csv.  The following needs to be deduced by the code from the data provided:
From Module Challenge:

•	The total number of months included in the dataset

•	The net total amount of "Profit/Losses" over the entire period

•	The changes in "Profit/Losses" over the entire period, and then the average of those changes

•	The greatest increase in profits (date and amount) over the entire period

•	The greatest decrease in profits (date and amount) over the entire period

Explanation of code step-by-step:

1.	Import pandas as pd  – importing pandas library and assigning pd as a variable

2.	Loading the data set from budget_data.csv by assigning file path and reading the budget_data.csv file through that file path in to the “data” dataframe
‘file_path = r"Module 3\Challenge\PyBank\Resources\budget_data.csv"
data = pd.read_csv(file_path)’

3.	Define code to get length of dataframe for the months column. This value provides the “The total number of months included in the dataset”.
`total_months = len(data)`

4.	Add all entries in Profit/Loss column to bring up a Net Total value. This value provides “The net total amount of "Profit/Losses" over the entire period”
` net_total = data['Profit/Losses'].sum()`

5.	The average change is defined by calculating the mean. This is the mean of the differences between Profit/Loss values. 
` avg_change = data['Profit/Losses'].diff().mean()`

6.	This is defined to find the greatest value of difference between the Profit/Loss values. 
` greatest_increase = data['Profit/Losses'].diff().max()`

7.	Defined to look for the corresponding date value for the highest indexed value in Profit/Loss values.
` greatest_increase_date = data.loc[data['Profit/Losses'].idxmax(), 'Date']`

8.	Defined to find the greatest decreased value between Profit/Loss values.
` greatest_decrease = data['Profit/Losses'].diff().min()`

9.	Looking for corresponding date value for greatest indexed decrease value in Profit/Loss values. 
` greatest_decrease_date = data.loc[data['Profit/Losses'].idxmin(), 'Date']`

10.	The following code has been commented out but was written to test if the code is working locally on the terminal. 

  `# Print Analysis to test if code is working on Visual Studio. Please note: The following is commented out to keep code clean and output directly to txt file.

  `# print("Financial Analysis")`
  
  `# print("----------------------------")`
  
  `# print(f"Total Months: {total_months}")`
  
 ` # print(f"Total: ${net_total}")`
 
  `# print(f"Average Change: ${avg_change:.2f}")`
  
  `# print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")`
  
  `# print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")`

11.	Defined printing results to budget_data.txt file.
    `output_file_path = r"C:\Users\shrut\OneDrive\Desktop\Bootcamp\Module 3\Challenge\python-challenge\Analysis\budget_data.txt"
    with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${avg_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")`

# PyPoll Challenge

## Problem Statement:

Using data provided in election_data.csv to determine the following.
From Module Challenge:

•	The total number of votes cast

•	A complete list of candidates who received votes

•	The percentage of votes each candidate won

•	The total number of votes each candidate won

•	The winner of the election based on popular vote

Explanation of code step-by-step:

1.	Step 1 and 2 from the previous challenge serve the same logic for this challenge as well. 

2.	Calculating total votes count by reading length of the dataframe 
` total_votes = len(election_data)`

3.	Defining unique entry in the “Candidate” column to determine remaining unique value. Essentially removing duplicates. 
` unique_candidates = election_data["Candidate"].unique()`

4.	Defining empty dictionary to store each candidates votes count
` candidate_votes = {}`

5.	Starts a loop to go through each unique candidate as defined in the syntax.
` for candidate in unique_candidates:`

6.	Captures votes counts for each candidate and places in defined “candidate_votes” dictionary. The logic here is:
7.	
a.	The code checks if the candidate value is equal to the candidate value defined in the loop, which is “unique_candidates”.

b.	The code filters only those rows in the dataframe where the candidate name is equal to the candidate name defined in the loop. 

c.	Calculates the length of the filtered data from above and stores in the pre-defined “candidate_votes” dictionary.
` candidate_votes[candidate] = len(election_data[election_data["Candidate"] == candidate])`


9.	The following code has been commented out but was written to test if the code is working locally on the terminal. 

  `# Print the election results to Visual code to test if code is working. Please note: The following is commented out to keep code clean and output directly to txt file.` 
  
  `#print("Election Results")`
  
  `#print("-------------------------")`
  
  `#print(f"Total Votes: {total_votes}")`
  
  `#print("-------------------------")`

9.	Second loop is defined to loop through “unique_candidate” values and evaluate their corresponding percentage of votes and votes count values. Please note: As noticed in how the data is to be presented, the percentage value has 3 decimal places which is defined in the code. 
` for candidate in unique_candidates:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    (f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})")`

9.Finally evaluating the winner of the polls.
`winner = max(candidate_votes, key=candidate_votes.get)`

10. The following code has been commented out but was written to test if the code is working locally on the terminal. 
  
   `#print("-------------------------")`
   
   `#print(f"Winner: {winner}")`
   
   `#print("-------------------------")`


11.	The following code defined output to the election_data.txt file. 

    `output_file_path = r"C:\Users\shrut\OneDrive\Desktop\Bootcamp\Module 3\Challenge\python-challenge\Analysis\election_data.txt"
    with open(output_file_path, 'w') as output_file:
   `# Writing election results to the file`
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
   
    `# Writting candidate information to file`
    for candidate in unique_candidates:
        percentage = (candidate_votes[candidate] / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})\n")
   
    output_file.write("-------------------------\n")
    
    `# Writing the winner to the file`
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")


