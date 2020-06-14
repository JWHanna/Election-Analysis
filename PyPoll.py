# Program Outline
# 1. The total number of votes
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


# Add dependencies
import csv
import os

# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Count total votes
total_votes = 0

# 2. List candidates
candidate_options = []

# Create a dictionary containing the candidate name, and the number of votes for that candidate
candidate_votes = {}

# 5. Determine winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Iterate through each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        # Find candiate name from ewach row
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            # Add candidate name to the list if it hasn't been recorded already
            candidate_options.append(candidate_name)

            # Begin tracking candidates vote count
            candidate_votes[candidate_name] = 0
        
        # Add vote to candidates vote count
        candidate_votes[candidate_name] += 1

# Save the results to a text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Iterate through the candidate list
    for candidate in candidate_options:
        # Retrieve the vote count for each candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of voted for each candidate
        vote_percentage = int(votes) / int(total_votes) * 100
        
        # Print & save the candidate name & percentage of votes to the text file
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)
        print(candidate_results)

        #Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning candidate equal to the candidate's name
            winning_candidate = candidate
    
    # Print & and save winning candidate data to the text file
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)