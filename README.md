# Nasa vs Aliens - Spaceship Game

## Project Goals

-   The main goal with this project is demonstrate the power of python programing language, and how simple it is to implement a
    basic application concept.

-   Nasa vs Aliens is a game developed to bring back the nostalgia of the 80s and 90s 2d games. This application target is mostly
    people that enjoy a good, light old fashioned game to pass the time or simply for the act of socializing.

 <img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/game_screen_shot%20-%20Copy.jpg">

live heroku link here

## Features

#### Existing Features

-   Health Status

 <img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/health_status.jpg">

Visible through out each match, shows players the status of their ship. Each player has 10 life points,
whenever a player reaches 0 the game is restarted.

#### Two Player Game

Players can share the same keyboard in order to play a match.

1. The left player uses the following keys:

-   UP --> W
-   DOWN --> S
-   LEFT --> A
-   RIGHT --> D
-   SHOOT --> SPACE-BAR

 <img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/bullets.jpg">

2. The right player uses the following keys:

-   UP --> ARROW UP
-   DOWN --> ARROW DOWN
-   LEFT --> ARROW LEFT
-   RIGHT --> ARROW RIGHT
-   SHOOT --> RIGHT CTRL

#### Winner Text

-   Each time the opposite side reaches 0 health the winner is announced.

 <img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/winner_text.jpg">

#### Features Left to Implement

1. In a near future I would like to implement a intro that presents the game.
2. Add a menu that let players choose their game character.

## Testing

The validator have not shown any big errors with the code, except for some warnings that have been ignored:

-   E231:11:21:missing whitespace after ','
-   E231:52:61:missing whitespace after ','
-   E501:52:80:line too long (95 > 79 characters)
-   E501:57:80:line too long (97 > 79 characters)
-   E501:61:80:line too long (95 > 79 characters)
-   E231:61:87:missing whitespace after ','
-   E302:64:1:expected 2 blank lines, found 1
-   E501:64:80:line too long (90 > 79 characters)
-   E261:69:33:at least two spaces before inline comment
-   E501:71:80:line too long (96 > 79 characters)
-   E261:71:81:at least two spaces before inline comment
-   E501:72:80:line too long (96 > 79 characters)
-   E261:72:81:at least two spaces before inline comment
-   E225:74:71:missing whitespace around operator
-   E501:74:80:line too long (80 > 79 characters)
-   E261:75:47:at least two spaces before inline comment
-   E261:76:50:at least two spaces before inline comment
-   E302:87:1:expected 2 blank lines, found 1
-   E261:93:54:at least two spaces before inline comment
-   E261:95:74:at least two spaces before inline comment
-   E501:95:80:line too long (81 > 79 characters)
-   E261:97:54:at least two spaces before inline comment
-   E261:99:73:at least two spaces before inline comment
-   E302:103:1:expected 2 blank lines, found 1
-   E261:109:80:at least two spaces before inline comment
-   E501:109:80:line too long (86 > 79 characters)
-   E261:111:77:at least two spaces before inline comment
-   E501:111:80:line too long (84 > 79 characters)
-   E261:113:56:at least two spaces before inline comment
-   E501:115:80:line too long (89 > 79 characters)
-   E261:115:83:at least two spaces before inline comment
-   E302:119:1:expected 2 blank lines, found 1
-   E302:140:1:expected 2 blank lines, found 1
-   E501:145:80:line too long (100 > 79 characters)
-   E302:150:1:expected 2 blank lines, found 1
-   E501:173:80:line too long (83 > 79 characters)
-   E501:174:80:line too long (97 > 79 characters)
-   E501:178:80:line too long (84 > 79 characters)
-   E501:179:80:line too long (87 > 79 characters)
-   E222:192:26:multiple spaces after operator
-   E303:200:9:too many blank lines (2)
-   E501:205:80:line too long (93 > 79 characters)

### Validator Testing

The code for this program was tested using the [PEP8 - validator](Assets\Validating\PEP8.txt)
and [Codeac - validator](https://app.codeac.io/github/fdasabino/Project_python_mls3).
No major issues were found with code.
