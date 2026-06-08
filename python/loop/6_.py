

# You want to simulate tea heating.
# It starts at 40°C and boils at 100°C.
# Task:

# * Use a `while` loop.
# * Increase temperature by 15 until it reaches or exceeds 100.
# * Print each temperature step.
temp = 40
while temp < 100:
    print(f"The current temp is: {temp}")
    temp +=15

print(f"The temp has reached at its final step {temp}")
