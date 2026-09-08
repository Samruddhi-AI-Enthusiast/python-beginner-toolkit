print("===== BILL SPLITTER =====")

bill = float(input("Enter total bill: ₹"))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print("\n----- BILL SUMMARY -----")
print("Original Bill: ₹", round(bill, 2))
print("Tip Amount: ₹", round(tip, 2))
print("Total Bill: ₹", round(total, 2))
print("Each Person Pays: ₹", round(per_person, 2))