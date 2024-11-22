
import os

import csv

# Set path for file
filepath = os.path.join('..','/Users/richardwillet/Desktop/Starter_Code-5/PyBank/Resources/budget_data.csv')

# Initialize variables
total_months = 0 
total_profit_losses = 0
previous_profit_losses = 0
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]


# Open the CSV
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


 # Loop through the rows
    for row in csvreader:
        # Update total months and total profit/losses
        total_months += 1
        total_profit_losses += int(row[1])

        # Calculate monthly change in profit/losses
        if total_months > 1:
            monthly_change = int(row[1]) - previous_profit_losses
            monthly_changes.append(monthly_change)

            # Update greatest increase and decrease
            if monthly_change > greatest_increase[1]:
                greatest_increase = [row[0], monthly_change]
            if monthly_change < greatest_decrease[1]:
                greatest_decrease = [row[0], monthly_change]

        previous_profit_losses = int(row[1])

# Calculate the average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Print the financial analysis
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


# Export the financial analysis to a text file
filepath = os.path.join('..', 'python-challenge', 'financial_analysis.txt')
with open(filepath, "w") as text_file:
    print('financial analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_profit_losses}', file=text_file)
    print(f'Average Change: ${average_change:.2f}', file=text_file)
    print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})', file=text_file)
    print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})', file=text_file)


