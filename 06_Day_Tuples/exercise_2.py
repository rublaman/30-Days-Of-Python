# Unpack siblings and parents from family_members
family_members = ('Marta', 'Ruben', 'Cipri', 'Esther')
siblings = family_members[0:2]
parents = family_members[2:]
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Orange', 'Watermelon', 'Test')
vegetables = ('Lettuce', 'Carrot', 'Tomatoe')
animal = ('Cat', 'Dot', 'Horse')
food_stuff_tp = fruits + vegetables + animal
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
slice_food_stuff_tp = food_stuff_tp[(len(food_stuff_tp) // 2) - 1]
# Slice out the first three items and the last three items from food_staff_lt list
slice_first_three_items = food_stuff_tp[0:3]
slice_last_three_items = food_stuff_tp[-3:]
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
