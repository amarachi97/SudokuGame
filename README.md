# SudokuGame
DESCRIPTION<br />
This is a python implementation of the classic sudoku game. The point of the game is to fill up the empty spaces with a number between 1 and 9, both included, while making sure that no numbers are repeated in the row, column or square. It was made using python and the pygame class for the GUI. Backtracking was also utilized for solving a valid sudoku. 

CODE EXECUTION<br />
The beginning of the class starts at board.py. During its execution, it calls the create.py class to create a unique sudoku and calls the solve_sudoku.py to solve the puzzle at the request of the user. 

INSTRUCTION<br />
Start by runnig the board.py class. In the console, the user is prompted to enter the desired level of difficulty;<br />
  1 - for easy<br />
  2 - for medium<br />
  3 - for hard. <br />
After this is specified the board is created with the puzzle waiting to be filled out. Now the user can click on the empty space they want to fill. After entering the desired number, the user can press the enter key to process their entry. If the entry is not a valid input, the input will remain RED. Otherwise, it will turn BLACK. 
NOTE that a valid input is one that is not repeated in the row, column or square. If at any point the user wants to delete an already processed input, the 'd' button is pressed to remove it and enter something else. If at some point the puzzle has become too difficult to solve, the user can press the 's' button for the computer to solve the puzzle. If what was filled out was correct, a message box will appear with the words "YOU WON!". The program also displays the time taken for the computer to solve the puzzle. Throughout the game, there is a timer that is running as the user fills out the puzzle. Once again, these are the valid commands:<br />
    d - to delete a previously processed input. This is an input is now BLUE <br />
    ENTER - to enter an input after it has been typed <br />
    s - to solve the button. <br />
After the user is done played, close the window to end the game

BUGS<br />
1. The window might not load up as expected if run too soon after the previous execution. Whatever the case may be, just start the execution over again.
2. Also solved time might have a negative value in the "seconds" portion of the display. I think this is because the puzzled was solved to soon after the gamke started, but I'm not sure.

POTENTIAL IMPROVEMENTS<br />
1. Might add a functionality to display the step by step solving of the game instead of just the finished product 
