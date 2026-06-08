

# Some chai flavors are out of stock.
# You want to skip those and stop entirely if someone requests a restricted flavor.
# Task:

# * Skip if flavor is "Out of Stock"
# * Break if flavor is "Discontinued"

chai  = ["green","pop","mom","sona","ginger","coppo"]

for item in chai:
   
   
    if item == "green":
        continue
    if item == "ginger":
        break
    
    print(f"item: #{item}")
    
print("The loop is ended")
# green, pop, mom, sona, ginger
# pop, mom, sona,