### Module 3 Challenge

## PyBank Challenge

# Problem Statement:

Create Python script to analyze financial records from data given in budget_data.csv.  The following needs to be deduced by the code from the data provided:
From Module Challenge:

•	The total number of months included in the dataset

•	The net total amount of "Profit/Losses" over the entire period

•	The changes in "Profit/Losses" over the entire period, and then the average of those changes

•	The greatest increase in profits (date and amount) over the entire period

•	The greatest decrease in profits (date and amount) over the entire period

Explanation of code step-by-step:

1.	Import CSV

2.	Loading the data set from budget_data.csv by assigning file path and reading the budget_data.csv file through that file path in to the “data” 

	‘file_path = r"Module 3\Challenge\PyBank\Resources\budget_data.csv"  
 	with open(file_path, 'r') as file:
 	reader = csv.DictReader(file)
 	data = list(reader)`

3.	Creating csv reader using “DictReader” this will enable the csv first row to headers and each row as a dictionary

4.	Defining variables that are analyzed outputs of the data. The initial values have been assigned to zero to later subsequently add corresponding values. 

5.	The “for loop” will loop through each months data

	`for i in range(total_months):`

6.	Profit\Loss data values converted to integers

	`profit_loss = int(data[i]["Profit/Losses"])`
7.	Profit\Loss values are subsequently added for each month to update the “net_total” value

	`net_total += profit_loss`

8.	The “if” statement ensures that the running change is calculated from the second month and subsequently calculates change in profit\loss from previous month

	`if i > 0:
        	change = profit_loss - int(data[i - 1]["Profit/Losses"])
   		avg_change += change`

9.	The above change information is subsequently updated to reflect the most recent greatest change otherwise same logic applies to greatest decrease where the change is smaller that its last posted change value. The output also posts the corresponding dates for both change types. 

	`if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = data[i]["Date"]
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = data[i]["Date"]`

10.	Finally, the “avg_change” is calculated by dividing the total change by the total number of months (minus one – not considering the first month)

	`avg_change /= (total_months - 1)`

11.	The following code is commented out but was used to check if its working locally in the terminal. Instead the following code is used to output the results directly in to the budget_data.txt file. 

	`# Print Analysis to test if code is working on Visual Studio. Please note: The following is commented out to keep code clean. Output is written directly to txt file. `
	`#print("Financial Analysis")`
	`#print("----------------------------")`
	`#print(f"Total Months: {total_months}")`
	`#print(f"Total: ${net_total}")`
	`#print(f"Average Change: ${average_change:.2f}")`
	`#print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")`
	`#print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")`

12.	The output is then defined to be printed in to the budget_data.txt file.

	`output_file_path = r"C:\Users\shrut\OneDrive\Desktop\Bootcamp\Module 3\Challenge\python-challenge\Analysis\budget_data.txt"  
	with open(output_file_path, 'w') as output_file:
    	output_file.write("Financial Analysis\n")
    	output_file.write("----------------------------\n")
    	output_file.write(f"Total Months: {total_months}\n")
    	output_file.write(f"Total: ${net_total}\n")
   	output_file.write(f"Average Change: ${avg_change:.2f}\n")
    	output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    	output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")`

## PyPoll Challenge

# Problem Statement:

Using data provided in election_data.csv to determine the following.
From Module Challenge:

•	The total number of votes cast

•	A complete list of candidates who received votes

•	The percentage of votes each candidate won

•	The total number of votes each candidate won

•	The winner of the election based on popular vote

Explanation of code step-by-step:

1.	Step 1, 2, and 3 from the previous challenge serve the same logic for this challenge as well. 

2.	Formatting “header” to remove spaces from first line of the file and uses commas as separators between headers.

	`header = lines[0].strip().split(',')`

3.	The “Dict” function is used to create dictionaries which represents each row of the file. The “zip’ function creates pairs between the header and each line and the “Dict” function  then creates dictionaries of 	those pairs.  

	`election_data = [dict(zip(header, line.strip().split(','))) for line in lines[1:]]`

4.	Code defined to read length of data to get total votes

	`total_votes = len(election_data)`

5.	Defining empty dictionary to hold votes for unique_candidates

	`candidate_votes = {}`

6.	The “for loop” function loops through each dictionary in the “election_data” dataset. It checks if the candidate is present in the “unique_candidate” dictionary and adds a vote otherwise adds the candidate and 	the vote. 

	`for entry in election_data:
    		unique_candidate = entry["Candidate"]
    		if unique_candidate in candidate_votes:
        	candidate_votes[unique_candidate] += 1
    	else:
        	candidate_votes[unique_candidate] = 1`

13.	The following code is commented out but was used to check if its working locally in the terminal. Instead the following code is used to output the results directly in to the election_data.txt file. 

	`# Print the election results`
  	`# print("Election Results")`
 	`# print("-------------------------")`
 	`# print(f"Total Votes: {total_votes}")`
 	`# print("-------------------------")`

14.	The second loop function determines the percentage of votes out of the total votes that each unique candidate received and presented to three decimal places

	`for candidate, votes in candidate_votes.items():
    		percentage = (votes / total_votes) * 100
    		(f"{candidate}: {percentage:.3f}% ({votes})")`

15.	The winner is determined by calculating the candidate with the maximum number of votes received

	` winner = max(candidate_votes, key=candidate_votes.get)`

16.	Finally, the output path is defined to write the results to election_data.txt

	`for candidate, votes in candidate_votes.items():
        	percentage = (votes / total_votes) * 100
        	output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        	output_file.write("-------------------------\n")
    		output_file.write(f"Winner: {winner}\n")
    		output_file.write("-------------------------\n")`
