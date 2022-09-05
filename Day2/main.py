print("Welcome to the Tip Calculator!")

total_bill = input("What was the total bill?\n")

tip = input("How much tip would you like to give? 10, 12, or 15 %?\n")

people_to_split = input("How many people will split the bill?\n")

tip_converted = float(tip)/100

percentage = float(total_bill) * tip_converted

total_amount_with_tip = float(total_bill) + percentage

bill_split = total_amount_with_tip / int(people_to_split)

final_bill = round(bill_split, 2)

print(f"Each person should pay: $ {round(final_bill):.2f}")
