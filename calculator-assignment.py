print("Calculating total damage output considering new build variables.")
print("You will enter: Raw damage value of weapon, percent increase.")
raw_damage_input = float(input("Enter raw damage value of weapon: "))


def new_change_number(raw_damage_input, item_damage_change):
    result = raw_damage_input * (1 + item_damage_change)
    return result

print("Would you like to enter a new item damage increase percent value?")
new_item_input = input("Enter Yes/No: ")
item_damage_change = 0

while new_item_input.upper() == "YES":
    if new_item_input.upper() == "YES":
        print("New Item Damage Modifier:")
        item_damage_1_input = float(input("Enter % value of damage increase "))
        item_damage_change = (item_damage_1_input / 100) + item_damage_change
        print("Would you like to enter a new item damage increase percent value?")
        new_item_input = input("Enter Yes/No: ")

print("Here is your total new damage output given gear:")
print(new_change_number(raw_damage_input, item_damage_change))
        
# print("New Item Damage Modifier")
# item_damage_1_input = input("Enter % value of damage increase")
# # This line conversts the STR into a FLOAT so we can apply the math.
# item_damage_1 = float(item_damage_1_input)
# # This line converts the percent into a decimal 
# item_damage_1_dec = item_damage_1 / 100