"""
Enter take home pay and savings rate and investment percentages to get amount to be invested
"""
take_home = float(input("Enter take home pay: "))
savings_rate = float(input("Enter savings rate out of 100: "))
equity_allocation = float(input("Enter percentage allocation for equity: "))
debt_allocation = 100 - equity_allocation
large_cap_allocation = float(input("Enter percentage allocation for large cap within equity: "))
mid_cap_allocation = float(input("Enter percentage allocation for mid cap within equity: "))
small_cap_allocation = 100 - (large_cap_allocation + mid_cap_allocation)
savings_amount = (take_home * savings_rate)/100
equity_amount = (savings_amount * equity_allocation)/100
debt_amount = (savings_amount * debt_allocation)/100
large_cap_amount = (large_cap_allocation * equity_amount)/100
mid_cap_amount = (mid_cap_allocation * equity_amount)/100
small_cap_amount = (small_cap_allocation * equity_amount)/100
print(f"Large-cap investment: {large_cap_amount}")
print(f"Mid-cap investment: {mid_cap_amount}")
print(f"Small-cap investment: {small_cap_amount}")
print(f"Debt investment: {debt_amount}")