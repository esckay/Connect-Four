# Software Development Plan

------



### Purpose

The purpose of this app is to replicate the connect four game into a digital format within the terminal of a computer.



### Scope

------

Objective

In this current age, many of our forms of hard-copy media like books, newspapers, magazines, movies, shows and photos have transitioned into digital format. There are a few reasons for this transition to have occurred, with some of the reasoning that it is more convenient to store and there is an increase in ease of accessibility. It only stands to say that board games would fall into this category as well.



Audience

The audience is anyone who wishes to play a game of connect four. As a casual board game, the audience for this app isn't clearly defined since it's play time is not long and not complex. There is no age limitations with classifications, there isn't a required skillset to play this game and so conclusively this game isn't targeted at anyone in particular but created to be available for everyone. The logic behind the game is simple yet the maths behind the game is profound enough that it can be played to higher levels



Use of the app

As the app is opened up, it asks if you wish to play with a friend or against the AI. This launches the desired game mode of connect four.

#### How to play

------

Connect four is a very simple game which can last up to 42 moves and end up in a draw. The board layout comprises of 7 columns and 6 rows, with the players taking turns to drop a piece into a column. Pieces stack on top of one another so there may only be a singular piece within a spot of the board. Whichever player connects four individual pieces together (vertically, horizontally or diagonally wins). The game can either be won or in some cases even a draw state can be forced. 

*Hint: the player that starts off with the centre column can force a win!*

#### How to install

------



##### Features

##### Artificial Intelligence

------

This app has the ability to replicate a "user" to play against when there is no secondary player available.  Within this feature itself uses several functions to generate each part of the AI's logic.

The normal AI ascertains all possible present moves and assigns a value to each move, taking the highest scoring move. it checks all possible moves with COUNT functions with the use of RANGE. 

```python
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2
    elif window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4
```

The above represents the Ai looking at all possible moves and giving it a value. With the score being set to 5 when there are 3 pieces already in position the AI prioritises that move. The normal AI is purposely flawed so it is not deemed too smart. 

The smart AI built for this uses the function/algorithm named minimax to look at future possible moves otherwise named DEPTH in the following code. The 'deeper' you go the more possible moves you look at. 

```python
function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value
```

This is a version of pseudocode that was used to create the minimax function for the AI of this game.



##### Player Inputs

------

As a game, the app depends heavily on the player to input many times throughout the use of the app. As to combat any invalid inputs, each of the input functions within the game have validations lines created to "listen" for any unknown inputs. Using a variation of TRY and IF statements this has been possible to keep invalid inputs from causing the app to 'bug' out.  

```python
def player_one():
# player one turn with validation of input
    while True:
        try:
            col = input('Player 1 Which column would you like to place your piece? (0-6)?')
            val_one = int(col)
            if val_one >= 0 and val_one <= COLUMN_COUNT:
                break
            else:
                print("Invalid input, try again")
        except ValueError:
            print("Amount must be a number, try again")
    col = int(col)
    return col
```

The above is code pulled directly from the app that will be most heavily used . It represents the app asking for the player to select a column they would like to drop their piece into. With columns starting from 0 up to 6 (making a total of 7) columns available to choose from. COLUMN_COUNT has been defined as 7 at the initialisation of the app itself. 

#### Control flow diagram

------

![MainApp](docs/MainApp.jpg)

Initial thought of how the flow of the main display would function.

![GameFlow](docs/GameFlow.jpg)

As the game logic was being developed this flow was more fleshed out as more steps were required

![AIFlow](docs/AIFlow.jpg)

The AI logic flow appears to be simple in the flow chart however is more complex as you dig into it.



#### Trello board

![Last trello](docs/Last trello.png)

A look of the trello board that I created with possible ideas of app ideas that could be within this app. Despite the usefulness of trello I found it somewhat cumbersome to use as a checklist app for this current iteration of app/coding project however can see the usefulness further down the line



#### Development log

------



**29/06**

Having decided that connect 4 would be a fun and enjoyable project/game to work on delved into the maths behind the game. Found a lot of interesting information however did not apply it all to this app. Finished coding the player vs player side of the game as this was the simpler side of the project. Didn't encounter too many difficulties with the basics of this code however still have to look at cleaning the representation of the board

**5/07**

Bit more research into AI logic of connect 4 and was able to finish the code off. Changing game-modes within the app did cause me a few moments of wondering what happened however that has been cleaned up and is functioning as in tented. Cleaning up the main flow of the app and finishing off log/readme files left to do. Installer part of python to be completed as well

**6/07**

 