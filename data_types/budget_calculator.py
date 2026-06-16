monthly_income = float(input("Enter the Monthly Income: "))
rent_percentage = float(input("Enter the percentage of income allocated for Rent: "))
print(f"Calculating budget allocations...")
rent_budget = (monthly_income) * rent_percentage/100
print(f"Budget for Rent: ${rent_budget:.2f}")