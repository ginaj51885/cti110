#Variables and Expressions
#06/27/2022
#CTI-110 P2HW1-Meal Tip Tax Calculator
#Gina Jordan
#



food = float(input("Enter Food Cost: "))

tip_percent = float(input("Enter Tip Percentage: "))

tax_percent = float(input("Enter Tax Percentage: "))
total_cost = (food + tip_percent + tax_percent)


print("Calculated Tip: ",tip_percent)
print("Calculated Tax: ",tax_percent)
print("Total cost including tip and tax: ", total_cost)



