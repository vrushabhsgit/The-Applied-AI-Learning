# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosa, it confirms the order.
# Otherwise, it says it's not available.

# **Task:**

# * Take snack input
# * If it's `"cookies"` or `"samosa"`, confirm the order
# * Else, show unavailability

snack = input("Enter the snaack that you want: ").lower()
print("You selected snack:", snack)

if snack == "cookies" or snack =="samosa":
    print("Order confirmed")
else:
     print("sorry items are not avilable")  