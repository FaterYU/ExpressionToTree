# Report

## Contents

##  Basic Design For The Application

### Description

​	The application can change expression to binary tree and print it as readable image on terminal. In addition, it also can report the illegal expression and reload history expressions. The application's main file is ExpressionToBinaryTree.py, and it need run with python3.x. With more details, the application also has a unit test program.

#### Task Comment

##### Task 1

​	Instantiate an object from Expression's Class and use input function to read expression from shell which is user type and save it in a private variable which is a string type. Use eval function to calculated the result of expression and print it to the terminal.

##### Task 2

​	Firstly, change expression to Inverse Polish expression. With task's meaning, I need to create a binary tree from expression and Inverse Polish expression is helpful for changing, so split all the character in expression variable and make them as a Inverse Polish expression. 

​	Then, Inverse Polish expression can change to Binary Tree easily with Stack. 

​	At last, if I want to print the tree readable on the screen, I need to decide where I want to print,  terminal or GUI. Considering the compatibility of GUI or Qt execution in Linux, Windows and MacOS, printing it on terminal is a sensible decision. The example show the printing tree with tipping 90 degrees to the right, which is in task's description. I think if I print it vertical on the terminal, it will be understand more easily than printing horizontal. When I need to print it, I need to insert some space and line break into the tree's string. The amount of space is decided with the height of node, it can draw a conclusion that the amount of space in each line is geometric progression about height of node.

##### Task 3

​	At last task, printing the expression as a binary tree is solved. If I want to save the history expression, saving the origin expression is better than saving the tree. Thus, it just use a text file to save history expression in each line. When restart the program, user can choose the reload option to reload the expression and print it as a binary tree on terminal from the saving file.

##### Task 4

​	The task meaning is checking the expression and reporting why the expression is not valid. Because every expression is a string, I can checking them by using regular expression. That means if the expression match the wrong regex, I can say it is ' Not a valid expression, wrong number of operands'. 

##### Task 5

​	By using the package of unittest, I need to write a class inheriting TestCase. The test unit need to include every category of the input.

##### Task 6

​	