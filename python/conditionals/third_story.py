# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.

# **Task:**

# * Input: "small", "medium", "large"
# * Small $\rightarrow$ ₹10, Medium $\rightarrow$ ₹15, Large $\rightarrow$ ₹20
# * If invalid: show `"Unknown cup size"`

cup_size = input("Tell the cup size that you want: ").lower()
if cup_size == "small":
    print(f"price is ₹10")
elif cup_size == "medium":
    print(f"price is ₹15")
elif cup_size == "large":
    print(f"price is ₹20")
else:
    print(f"Unknown cup size")
