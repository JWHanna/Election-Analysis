# M3 Challenge
# Instructions:
    # - Create a list for the counties
    
    # - Create a dictionary where the county is the key 
    #   and the votes cast for each county in the election are the values.
    
    # - Create an empty string that will hold the county name that had 
    #   the largest turnout.
    
    # - Declare a variable that represents the number of votes that a county recieved.
    
    # - Inside the with open() function where you are outputting the file, 
    #   do the following:  
        # - Create three if statements to print out the voter turnout results similar 
        #   to the results shown.
        # - Add the results to the output file.
        # - Print the results in the command line.

# Program Outline
# 1. Calculate the total number of votes
# 2. Create a complete list of candidates who recieved votes
# 3. Calculate the percentage of votes each candidate won
# 4. Calculate the total number of votes each candidate won
# 5. Determine the winner of the election based on popular vote
# 6. Calculate the number of votes per county
# 7. Calculate the percent of the total vote that each county accounts for


# Add dependencies
import csv
import os

# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Count total votes
total_votes = 0

# List candidates
candidate_options = []

# Create a dictionary containing the candidate name, 
# and the number of votes for that candidate
candidate_votes = {}

# Determine winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# List counties
counties = []

# Create a dictionary containing the county name,
# and the number of votes from that county
county_votes = {}

# Determine county with largest turnout
largest_turnout_county = ""
largest_turnout_count = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Iterate through each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        # Find candiate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add candidate name to the list if it hasn't been recorded already
            candidate_options.append(candidate_name)

            # Begin tracking candidates vote count
            candidate_votes[candidate_name] = 0
        
        # Add vote to candidates vote count
        candidate_votes[candidate_name] += 1

        # Find county from each row
        county_name = row[1]
        if county_name not in counties:
            # Add county name to the list if it hasnt been recorded already
            counties.append(county_name)

            #Begin tracking county vote count
            county_votes[county_name] = 0
        
        # Add vote to county vote count
        county_votes[county_name] += 1

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

    # Print & save section header to text file
    county_vote_header = "County Votes:\n"
    print(county_vote_header)
    txt_file.write(county_vote_header)
    
    # Iterate through the counties list
    for county in counties:
        # Retrieve the vote count for each county
        county_vote_count = county_votes[county]
        # Calculate the percentage of the total vote that each county accounts for
        county_vote_percentage = int(county_vote_count) / int(total_votes) * 100

        # Print and save county turnout data to text file
        county_turnout = (f"{county}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_turnout, end="")
        txt_file.write(county_turnout)
        
    
    # Determine largest turnout
        if (county_vote_count > largest_turnout_count):
            # If true then set largest_turnout = county_vote_count
            largest_turnout_count = county_vote_count
            # Set largest_turnout_count equal to largest_turnout_county
            largest_turnout_county = county

    largest_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county} ({largest_turnout_count:,})\n"
        f"-------------------------\n")
    print(largest_turnout_summary, end="")
    txt_file.write(largest_turnout_summary)
    

    # Iterate through the candidate list
    for candidate in candidate_options:
        # Retrieve the vote count for each candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of voted for each candidate
        vote_percentage = int(votes) / int(total_votes) * 100
        
        # Print & save the candidate name & percentage of votes to the text file
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)
        

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
    print(winning_candidate_summary, end="")
    txt_file.write(winning_candidate_summary)
    