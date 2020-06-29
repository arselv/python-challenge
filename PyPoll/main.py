# PyPoll HW
# Allow to create file path across operating systems
import os

# Module reading csv file
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('analysis', 'election_data.txt')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_voter_count = 0
    khan_count = 0
    correy_count = 0
    li_count = 0
    o_tooley_count = 0

    for row in csvreader:

        # Candidate set to candidate name in row
        candidate = row[2]

        # Check which candidate was chosen and keep count
        if candidate == 'Khan':
            khan_count = khan_count + 1

        elif candidate == 'Correy':
            correy_count = correy_count + 1

        elif candidate == 'Li':
            li_count = li_count + 1

        elif candidate == 'O\'Tooley':
            o_tooley_count = o_tooley_count + 1
            
        # Keeping count of number of votes
        total_voter_count = total_voter_count + 1

    # Calculating voting percentage for each candidate
    khan_percentage = (khan_count / total_voter_count) * 100
    correy_percentage = (correy_count / total_voter_count) * 100
    li_percentage = (li_count / total_voter_count) * 100
    o_tooley_percentage = (o_tooley_count / total_voter_count) * 100
    
    # Declaring a winner by voter count
    if khan_count > correy_count > li_count > o_tooley_count:
        winner = 'Khan'

    elif correy_count > khan_count > li_count > o_tooley_count:
        winner = 'Correy'

    elif li_count > khan_count > correy_count > o_tooley_count:
        winner = 'Li'
    
    else:
        winner = 'O\'Tooley'
    
    # Terminal Printout
    print(f'Elections Results\n'+'-----------------------\n'+
        f'Total Votes: {total_voter_count}\n'+
        f'-----------------------\n'+
        f'Khan: {round(khan_percentage, 3)}% ({khan_count})\n'+
        f'Correy: {round(correy_percentage, 3)}% ({correy_count})\n'+
        f'Li: {round(li_percentage, 3)}% ({li_count})\n'+
        f'O\'Tooley: {round(o_tooley_percentage, 3)}% ({o_tooley_count})\n'+
        f'-----------------------\n'+
        f'Winner: {winner}\n'+
        f'-----------------------')

    # Text file printout
    output_file = open(output_path, "w")
    output_file.write(
        f'Elections Results\n'+'-----------------------\n'+
        f'Total Votes: {total_voter_count}\n'+
        f'-----------------------\n'+
        f'Khan: {round(khan_percentage, 3)}% ({khan_count})\n'+
        f'Correy: {round(correy_percentage, 3)}% ({correy_count})\n'+
        f'Li: {round(li_percentage, 3)}% ({li_count})\n'+
        f'O\'Tooley: {round(o_tooley_percentage, 3)}% ({o_tooley_count})\n'+
        f'-----------------------\n'+
        f'Winner: {winner}\n'+
        f'-----------------------')
    output_file.close()

