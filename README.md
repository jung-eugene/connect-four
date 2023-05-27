# Connect Four 🎰

A Connect Four game built in Python. I created a class that represents the board for a game of Connect Four, and also an AI player that the user can play against.

## How Connect Four Works 🎲

Connect Four is a variation of tic-tac-toe played on a 6x7 rectangular board:

The game is played by two players, and the goal is to place four checkers in a row vertically, horizontally, or diagonally. The players alternate turns and add one checker to the board at a time. However, because the board stands vertically, a checker cannot be placed in an arbitrary position on the board. Rather, a checker must be inserted at the top of one of the columns, and it “drops down” as far as it can go – until it rests on top of the existing checkers in that column, or (if it is the first checker in that column) until it reaches the bottom row of the column.

The standard board size for Connect Four is six rows of seven columns, but my Board class can handle boards of any dimensions. However, for simplicity, I  preserved the four-in-a-row requirement for winning the game regardless of the board size (even for boards with dimensions less than 4x4).

###### Part of Boston University CS 111 Coursework
