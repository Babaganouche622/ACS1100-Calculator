print("Calculating total damage output considering new build variables.")
print("You will enter: Raw damage value of weapon, percent increase.")
raw_damage_input = float(input("Enter raw damage value of weapon: "))

# I made this new class to keep all my math at the top of the code.
# I figured this would be a good thing if my code were to run long so I could find it easily.
def new_change_number(raw_damage_input, item_damage_change):
    result = raw_damage_input * (1 + item_damage_change)
    return result

# This is to start my loop.
print("Would you like to enter a new item damage increase percent value?")
new_item_input = input("Enter Yes/No: ")
# I had to set the variable to an int value so I could then reasign it's value later on in the loop.
item_damage_change = 0

# I can't believe I got this loop to work! Josh and I jumped out of our seats when it printed the math. 
# Arguably outside of the scope of the project, but I wanted a way for the number of variable entries to not matter.
while new_item_input.upper() == "YES":
    if new_item_input.upper() == "YES":
        print("New Item Damage Modifier:")
        item_damage_input = float(input("Enter % value of damage increase "))
        item_damage_change = (item_damage_input / 100) + item_damage_change
        print("Would you like to enter a new item damage increase percent value?")
        new_item_input = input("Enter Yes/No: ")

print("Here is your total new damage output given gear:")
print(new_change_number(raw_damage_input, item_damage_change))
        