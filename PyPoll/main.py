# Load dataset from election_data.CSV file
file_path = r"Module 3\Challenge\python-challenge\Resources\election_data.csv"

# Read data from the CSV file and store it in a list of dictionaries
with open(file_path, 'r') as file:
    lines = file.readlines()
    header = lines[0].strip().split(',')
    election_data = [dict(zip(header, line.strip().split(','))) for line in lines[1:]]

# Calculate the total number of votes
total_votes = len(election_data)

# Define dictionary to store candidate votes
candidate_votes = {}

# Loop through data to count votes for each candidate
for entry in election_data:
    unique_candidate = entry["Candidate"]
    if unique_candidate in candidate_votes:
        candidate_votes[unique_candidate] += 1
    else:
        candidate_votes[unique_candidate] = 1

# Print the election results
# print("Election Results")
# print("-------------------------")
# print(f"Total Votes: {total_votes}")
# print("-------------------------")

# Loop through candidates data and print their information
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    (f"{candidate}: {percentage:.3f}% ({votes})")

# Evaluate winning candidate with most votes
winner = max(candidate_votes, key=candidate_votes.get)
# print("-------------------------")
# print(f"Winner: {winner}")
# print("-------------------------")

# Define output file to election_data.txt
output_file_path = r"C:\Users\shrut\OneDrive\Desktop\Bootcamp\Module 3\Challenge\python-challenge\Analysis\election_data.txt"
with open(output_file_path, 'w') as output_file:
    # Writing election results to the file
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
   
    # Writing candidate information to file
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
   
    output_file.write("-------------------------\n")
    
    # Writing the winner to the file
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
