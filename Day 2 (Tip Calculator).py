print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? (%): ")
split_bill = input("How many people to split the bill? ")

#Convert str to float to use for math
total_bill = float(total_bill)
tip_percentage = float(tip_percentage)
split_bill = float(split_bill)

#Math for bill
percentage = (tip_percentage / 100)
add_on_bill = (percentage * total_bill)
bill_calculated = (total_bill + add_on_bill)

bill_split = (round(bill_calculated / split_bill, 2))
final_bill = "{:.2f}".format(bill_split)
print("Each person should pay: $", final_bill)

