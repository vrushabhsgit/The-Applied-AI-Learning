

# You're preparing an order summary with customer names and their total bill.
# Task:

# * Use two lists: one for names and one for bills.
# * Print: "[Name] paid ₹[amount]"

names = ['ram',"kisna","shankar","hanuman"]
amount = [100,200,300,400]

for names, amount in zip(names,amount):
    print(f"name: {names}, amount: {amount}")