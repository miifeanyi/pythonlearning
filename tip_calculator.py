#Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What is the total bill today? \n$"))
tip = int(input("What percentage of tip would you like to give? 5 10 12 15 20\n"))
people = int(input("How many people will split the bill?\n"))
tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")