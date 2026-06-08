# You run an online tea store.

# If the order amount is more than ₹300, delivery is free;
# otherwise, it costs ₹30.

# **Task:**

# * Input: `order_amount`
# * Use ternary operator to decide delivery fee

order_amount = float(input("Please tell us your order amount: "))
delivery_fee = "free" if order_amount > 300 else 30

print(f"delivery fee: {delivery_fee}")