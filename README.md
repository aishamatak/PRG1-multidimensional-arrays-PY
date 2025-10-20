# 2D Arrays - PRIMM Activities

## PREDICT - What will happen?

Before running any code, look at these examples and **predict** what you think will happen. Write down your predictions!

### Example 1: Basic 2D Array
```python
scores = [[78, 81, 84], [55, 54, 62], [89, 71, 90]]
print(scores[1][2])
print(len(scores))
print(len(scores[0]))
```
**Predict:** What will be printed? What does each line do?

### Example 2: Nested Loops
```python
grid = [[1, 2], [3, 4], [5, 6]]
total = 0
for row in grid:
    for number in row:
        total += number
print(f"Total: {total}")
```
**Predict:** What will the total be? How does the code calculate it?

### Example 3: Finding Maximum
```python
temperatures = [[12, 15, 18], [22, 25, 20], [16, 19, 21]]
max_temp = 0
for day in temperatures:
    for temp in day:
        if temp > max_temp:
            max_temp = temp
print(f"Highest temperature: {max_temp}")
```
**Predict:** What will be the highest temperature found?

## RUN - Test your predictions

Now run each code example above. Were your predictions correct? If not, what surprised you?

Create a new Python `.py` file and test each example. Note down what actually happened.

## INVESTIGATE - Explore the patterns

Use the sample code provided to investigate these questions:

### Investigation 1: Array Access
```python
activities = [
    ['Work', 9],
    ['Eat', 1], 
    ['Commute', 2],
    ['Play Game', 1],
    ['Sleep', 7]
]
```

Try these commands and explain what each does:
- `print(activities[0])`
- `print(activities[2][1])`  
- `print(activities[-1][0])`
- `print(len(activities))`

### Investigation 2: Different Loop Styles
Test these different ways to loop through the same 2D array:

**Style 1 - Direct iteration:**
```python
for activity in activities:
    print(activity[0], "takes", activity[1], "hours")
```

**Style 2 - Index-based:**
```python
for i in range(len(activities)):
    print(activities[i][0], "takes", activities[i][1], "hours")
```

**Style 3 - Nested indices:**
```python
for i in range(len(activities)): 0-4 (or 0-5 but dont include 5)
    for j in range(len(activities[i])): 0-1 (or 0-2 but dont include 2)
        print(f"Position [{i}][{j}] = {activities[i][j]}")
```

Which style do you prefer for different tasks? When might you use each?

## MODIFY - Change existing code

### Modify 1: Enhance the Temperature Tracker
Start with this code and make the requested changes:

```python
weekly_temps = [
    [12, 15, 18, 20, 17],  # Week 1
    [22, 25, 20, 19, 21],  # Week 2  
    [16, 19, 21, 23, 18]   # Week 3
]
```

**Your tasks:**
1. Modify the maximum finding code to also find the minimum temperature
2. Calculate and display the average temperature across all weeks
3. Add code to find which week had the highest average temperature
4. Add a new week of temperatures to the array

### Modify 2: Extend the Activities List
Using the activities array from Investigation 1:

1. Add code to calculate the total hours spent on all activities
2. Modify the percentage calculation to round to 1 decimal place instead of whole numbers
3. Add a new activity of your choice
4. Sort the activities by hours spent (highest first)

### Modify 3: The Flowers Challenge
Here's the flowers scenario with a small bug - can you fix it?

```python
plants = [
    ["Begonia", "Daisy", "Lily", "Peony", "Rose", "Sunflower", "Lavender"], 
    [1, 6, 3, 4, 5, None, 2]  # Note: None instead of null
]

current_element = 0
alphabetical_order = []

while current_element is not None:
    alphabetical_order.append(plants[0][current_element])
    current_element = plants[1][current_element]

print(" -> ".join(alphabetical_order))
```

**Your tasks:**
1. Run the code - does it work as expected?
2. If there are issues, identify and fix them
3. Modify it to also print the position number of each plant
4. Add a new plant "Iris" in the correct alphabetical position

## MAKE - Create from scratch

### Make 1: Student Gradebook
Create a 2D array to store student grades for different subjects:

**Requirements:**
- At least 4 students
- At least 3 subjects per student  
- Calculate each student's average
- Find the highest and lowest grade overall
- Determine which student has the best average

### Make 2: Simple Game Board
Create a basic game board (like tic-tac-toe but 4x4):

**Requirements:**
- Initialise an empty 4x4 board
- Create a function to display the board nicely
- Allow players to place 'X' or 'O' at specific coordinates
- Check if a position is already occupied
- Keep track of how many moves have been made

### Make 3: Weather Station Data
Create a program that simulates weather data collection:

**Requirements:**
- Store temperature and humidity for each day of a week
- Calculate daily averages
- Find the day with the most extreme weather (highest temperature difference from average)
- Create a simple weather report summary

### Make 4: Cinema Seating
Create a cinema seating system:

**Requirements:**
- Create a 2D array representing cinema seats (8 rows, 10 seats each)
- Use different symbols for available/booked seats
- Allow users to "book" specific seats
- Display the seating chart
- Calculate how many seats are still available

## Extension Challenges

### Challenge 1: Advanced Flowers
Extend the flowers scenario:
- Add more plants to make the list longer
- Create a function that can insert a new plant in the correct alphabetical position
- Modify the algorithm to print in reverse alphabetical order

### Challenge 2: Noughts and Crosses
Complete the noughts and crosses game:
- Implement win-checking logic (rows, columns, diagonals)
- Add input validation
- Keep score across multiple games
- Allow players to choose their symbols

### Challenge 3: Data Analysis
Create a program that analyses sales data:
```python
# Sales data: [Product, Week1, Week2, Week3, Week4]
sales_data = [
    ["Laptops", 15, 22, 18, 25],
    ["Phones", 30, 35, 28, 40], 
    ["Tablets", 12, 15, 20, 18]
]
```
- Find the best-selling product overall
- Calculate week-on-week growth rates
- Identify trends (increasing/decreasing sales)
- Create a summary report

Remember: The key to mastering 2D arrays is understanding how to navigate through rows and columns effectively. Practice different loop patterns and always think about what level (outer array vs inner array) you're working with!