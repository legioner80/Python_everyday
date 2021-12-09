print("Welcome to the tip and tax calculator!")
bill = float(input("What was the final bill? $"))
tax = 0.14975 * bill
final_bill = tax + bill
tip = int(input("What percentage would you like to tip?"))
people = int(input("How many people will split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = final_bill * tip_as_percent
total_bill = final_bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person would pay: ${final_amount} including 14.975% tax.")


