
# Calculating raw damage increase based on item % increase value
# If you have say 2 talismans that each boost damage by 15% value, how much total damage will you do?
print("Calculating total damage output considering new build variables.")
print("You will enter: Raw damage value of weapon, percent increase for 3 sources.")
raw_damage_input = input("Enter raw damage value of weapon")
raw_damage = float(raw_damage_input)


print("New Item Damage Modifier")
item_damage_1_input = input("Enter % value of damage increase")
# This line conversts the STR into a FLOAT so we can apply the math.
item_damage_1 = float(item_damage_1_input)
# This line converts the percent into a decimal 
item_damage_1_dec = item_damage_1 / 100

print("New Item Damage Modifier")
item_damage_2_input = input("Enter % value of damage increase")
item_damage_2 = float(item_damage_2_input)
item_damage_2_dec = item_damage_2 / 100

print("New Item Damage Modifier")
item_damage_3_input = input("Enter % value of damage increase")
item_damage_3 = float(item_damage_3_input)
item_damage_3_dec = item_damage_3 / 100

def new_damage_raw(raw_damage):
    changed_number = raw_damage * (1 + (item_damage_1_dec + item_damage_2_dec + item_damage_3_dec))
    return changed_number

print("Final total damage is:")
print(new_damage_raw(raw_damage))

# I really wanted to create an IF/ELSE function to have the user input a Yes/No bool to creat a new "New Item Damage Modifier"
# I really struggled figuring out how to get it to rename the new saved values that I gave up.
# This seemed out of the scope of this assignment right now but I'm really excited to learn more about IF statements!