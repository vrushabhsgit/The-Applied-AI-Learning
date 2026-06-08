

# You're building a ticket info system for a railway app.
# Based on seat type, show its features.

# **Task:**

# * Input: `"sleeper"`, `"AC"`, `"general"`, `"luxury"`
# * Match using `match-case`
# * Unknown $\rightarrow$ show: `"Invalid seat type"`

seat_type = input("Enter your seat type prefrence: ").lower()
match seat_type:
    case "general":
        print("feature 1")
    case "sleeper":
        print("feature 2")
    case "ac":
        print("feature 3")
    case "luxary":
        print("feature 4")
    case _:
        print("Invalid seat type")