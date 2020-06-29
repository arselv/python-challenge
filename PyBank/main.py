# PyBank HW
# Allow to creat file paths across operating systems
import os

# Module reading csv file
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', "budget_data.txt")


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_months = 0
    net_total = 0
    greatest_profit = 0
    greatest_loss = 0
    second = 0
    i = 1
    difference = 0
    difference_list = []
    
    for row in csvreader:
        
        # Using i as a lookahead for next row
        if i > 1:
            next_profitloss = int(row[1])
            #print(next_profitloss)
            
            #Calculate the change between current and previous month Profit/Loss
            difference =  next_profitloss - profit_loss
            difference_list.append(difference)

        # Assigns Column 1 to an integer variable, working
        profit_loss = int(row[1])

        #Sum of Profit/Losses Column 1, working
        net_total = net_total + profit_loss
    
        # Number of months, number rows minus header, working
        total_months = total_months + 1
        #print(total_months)
    
        # Find the greatest profit and associated date
        if profit_loss >= greatest_profit:
            greatest_profit = profit_loss
            greatest_profit_date = row[0]
        
        # Find the greatest loss and associated date
        if profit_loss <= greatest_loss:
            greatest_loss = profit_loss
            greatest_loss_date = row[0]
        
        i = i+1
        
    # Calculate change average
    average_change = sum(difference_list) / len(difference_list)

    # Display data set results to terminal
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total:  ${net_total}")
    print(f"Average Change:  ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits:  {greatest_profit_date} (${greatest_profit})")
    print(f"Greatest Decrease in Profits:  {greatest_loss_date} (${greatest_loss})")

    # Write data set results to .txt file   
    output_file = open(output_path, "w")
    output_file.write(
        "Financial Analysis\n"+
        "--------------------------\n"+
        f"Total Months: {total_months}\n"+
        f"Total:  ${net_total}\n"+
        f"Average Change:  ${round(average_change, 2)}\n"+
        f"Greatest Increase in Profits:  {greatest_profit_date} (${greatest_profit})\n"+
        f"Greatest Decrease in Profits:  {greatest_loss_date} (${greatest_loss})"
        )
    output_file.close()
