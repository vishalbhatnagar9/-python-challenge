import pandas as pd

# Load dataset from election_data.CSV file
file_path = r"Module 3\Challenge\python-challenge\Resources\election_data.csv"
election_data = pd.read_csv(file_path)

# Calculate the total number of votes by reading lenght of 
total_votes = len(election_data)

# Get a list of unique candidates
unique_candidates = election_data["Candidate"].unique()

# Define directory to store candidate votes
candidate_votes = {}

# Loop through data to count votes for each candidate 
for candidate in unique_candidates:
    candidate_votes[candidate] = len(election_data[election_data["Candidate"] == candidate])

# Print Analysis to test if code is working on Visual Studio. Please note: The following is commented out to keep code clean. Output is directly printed to txt file.  
#print("Election Results")
#print("-------------------------")
#print(f"Total Votes: {total_votes}")
#print("-------------------------")

# Loop through candidates data and print their information
for candidate in unique_candidates:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    (f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})")

# Evaluate winning candidate with most votes. Please note: The following is commented out to keep code clean and output directly to txt file. 
winner = max(candidate_votes, key=candidate_votes.get)
#print("-------------------------")
#print(f"Winner: {winner}")
#print("-------------------------")

# Define output file to election_data.txt
output_file_path = r"C:\Users\shrut\OneDrive\Desktop\Bootcamp\Module 3\Challenge\python-challenge\Analysis\election_data.txt"
with open(output_file_path, 'w') as output_file:
    # Writing election results to the file
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
   
    # Writting candidate information to file
    for candidate in unique_candidates:
        percentage = (candidate_votes[candidate] / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})\n")
   
    output_file.write("-------------------------\n")
    
    # Writting the winner to the file
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")




