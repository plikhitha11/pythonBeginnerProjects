import matplotlib.pyplot as plt

def calculate_tax(income):
    # Define tax brackets and rates for Indian Rupees (example values)
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05  # 5% tax on income over ₹2,50,000
    elif income <= 1000000:
        tax = (income - 500000) * 0.2 + 12500  # 20% tax on income over ₹5,00,000 plus ₹12,500
    else:
        tax = (income - 1000000) * 0.3 + 112500  # 30% tax on income over ₹10,00,000 plus ₹1,12,500

    return tax

# Input: Prompt user to enter their income
income_rupees = float(input("Enter your income in Indian Rupees: "))

# Calculate tax
tax_rupees = calculate_tax(income_rupees)

# Display the result using matplotlib
plt.figure(figsize=(6, 3))
plt.text(0.5, 0.5, f"Income: ₹{income_rupees:,.2f}\nTax: ₹{tax_rupees:,.2f}", fontsize=14, ha='center', va='center')
plt.axis('off')  # Turn off the axis
plt.show()
