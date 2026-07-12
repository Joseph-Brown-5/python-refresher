# a 2D list is a list made up of lists
# you can mix lists, so you can have a list of tuples or something similar

# each of these lists is a 1 demenstional list
# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# this is a 2D list
# groceries = [fruits, vegetables, meats]

# this is another way to make the same list
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# print(groceries)              # this will print all three sub lists out flat
# print(groceries[0])           # this will print out the "fruits" list or the first list in the parent list
# print(groceries[0][0])        # this will print out the first value of the first list

# to iterate over a 2D list use nested loops
for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()
