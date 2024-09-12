# 2D Array Activities Project(s)

(You can create a new blank py file for these)
Refer to the samples for help with syntax if you need.

## Beginner Challenge

1. Can you total the contents of a 2D array?
2. Can you calculate the average of a 2D array?
3. Can you calculate the maximum value stored within a 2D array?
4. Can you calculate the minimum value stored in a 2D array?
5. Can you create an array 10 by 10 that has zeros in each position?
6. Can you create a 2D array, 10 by 10 with numbers in it 1-100?
7. Could you shuffle the above array so that the numbers 1-100 are in random positions?


## Trickier Challenges

### Flowers Scenario

The 2D array below contains two rows and seven columns. The first row contains the names of plants. The second row contains a 'pointer' which 'points' to the next plant in alphabetical order. 

So, starting with Begonia, we notice that the pointer is 1, so we look at the value stored at position 1. We can see that it is Daisy. Daisy’s pointer is 6, so we now look at the value stored in position 6, and so on..

| Begonia | Daisy | Lily | Peony | Rose | Sunflower | Lavender |
|---------|-------|------|-------|------|-----------|----------|
| 1       | 6     | 3    | 4     | 5    | null      | 2        |


In Python, this looks like this:

```python
plants = [["Begonia", "Daisy", "Lily", "Peony", "Rose", "Sunflower", "Lavender"], [1,6,3,4,5,null,2]]
```

So, we can write an algorithm that uses the pointer values in row 1 to print out the list in alphabetical order, without changing the order of the flowers in the array: Begonia -> Daisy -> Lavender -> Lily -> Peony -> Rose -> Sunflower.

Here’s some pseudo code. Can you make it work in Python?

```
currentElement = 0

WHILE currentElement != "null" DO 
	OUTPUT plantList[0][currentElement]
	currentElement = plantList[1][CurrentElement]
ENDWHILE
```

### Noughts and Crosses Scenario

Here's an empty board:

```python
board = [
    ["", "", ""], // Row 1
    ["", "", ""], // Row 2
    ["", "", ""]  // Row 3
]
```

How about making a two-player noughts and crosses game?

* Start with a blank board
* Ask player 1 for a row and column where they'd like to place their symbol.
* Check if the space is empty
* If empty, add the player's symbol and print out the board again..
* Player 2 has their go..
* If you are feeling adventurous, you can add code to check to see if a player has won!
