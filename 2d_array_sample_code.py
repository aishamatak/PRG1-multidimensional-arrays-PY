# Iterating through a list
task = ["a", "b", "c", "d"]
for letter in task:
    print(letter)

# Multidimensional list
scores = [[78, 81, 84], [55, 54, 62], [89, 71, 90]]

# Sorting a list
tests = ["c", "b", "a"]
tests.sort()
print(tests)

# Length of a list
print(len(scores))

# Iterating through elements of a list
for score in scores:
    print(score)

# Nested iteration
for score in scores:
    for element in score:
        print(element)

# Index-based iteration
for i in range(len(scores)):
    print(scores[i])

# Nested index-based iteration
for i in range(len(scores)):
    for j in range(len(scores[i])):
        print(scores[i][j])

# Finding the maximum value
max_value = 0
for score in scores:
    for value in score:
        if value > max_value:
            max_value = value
print(max_value)

# Function to calculate the maximum value
def calculate_max_value(data):
    max_value = 0
    for row in data:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value

print(calculate_max_value(scores))


# Multidimensional list operations (comments translated)

# To declare an empty multidimensional list, you use the same syntax as declaring a one-dimensional list:
# activities = []

# Defines a two-dimensional list named activities
activities = [
    ['Work', 9],
    ['Eat', 1],
    ['Commute', 2],
    ['Play Game', 1],
    ['Sleep', 7]
]

print(activities[3][1])  # Output: 1

# To add a new element at the end of the multidimensional list, you use the append() method
activities.append(['Study', 2])

# To insert an element in the middle of the list, you use the insert() method. 
# The following inserts an element in the second position of the activities list:
activities.insert(1, ['Programming', 2])

# This example calculates the percentage of the hours spent on each activity and appends the percentage to the inner list.
for activity in activities:
    percentage = round((activity[1] / 24) * 100)
    activity.append(str(percentage) + '%')

# Pretty print the list
from pprint import pprint
pprint(activities)

# To remove an element from a list, you use the pop() or del method.
# The following statement removes the last element of the activities list
activities.pop()

# You can remove elements from the inner list of the multidimensional list by using the pop() method
# The following example removes the percentage element from the inner lists of the activities list
for activity in activities:
    activity.pop()

# To iterate a multidimensional list, you use a nested for loop

# Loop the outer list
for i in range(len(activities)):
    # Get the size of the inner list
    inner_array_length = len(activities[i])
    # Loop the inner list
    for j in range(inner_array_length):
        print(f'[{i},{j}] = {activities[i][j]}')

# Or you can use nested for loops directly
for activity in activities:
    for data in activity:
        print(data)

pprint(activities)
