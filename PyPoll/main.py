import os
import csv

# File path for the dataset
file_path = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the dataset
with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip header row
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Prepare the results
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
    if votes > winner["votes"]:
        winner = {"name": candidate, "votes": votes}

output += (
    "-------------------------\n"
    f"Winner: {winner['name']}\n"
    "-------------------------\n"
)

# Print to terminal
print(output)

# Save to text file
output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, "w") as file:
    file.write(output)
