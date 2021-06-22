# Nasa vs Aliens - Spaceship Game

## Project Goals

-   The main goal with this project is demonstrate the power of python programing language, and how simple it is to implement a
    basic application concept.

-   Nasa vs Aliens is a game developed to bring back the nostalgia of the 80s and 90s 2d games. This application target is mostly
    people that enjoy a good, light old fashioned game to pass the time or simply for the act of socializing.

 <img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/game_screen_shot%20-%20Copy.jpg">

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

## Testing [![Codeac](https://static.codeac.io/badges/2-377614318.svg "Codeac")](https://app.codeac.io/github/fdasabino/Project_python_mls3)

The error shown by the validator is located on the provided deployment files provided by the template owner.

The validator have shown some warnings with the code written, these warnings don't create any problems and were therefore ignored:

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

The code for this program was tested using the [PEP8 - validator](Assets\Validating\PEP8.txt) and [Codeac - validator](https://app.codeac.io/github/fdasabino/Project_python_mls3).
No major issues were found with code.

<img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/checker2.jpg">



## Deployment

- The files have been published on a [Replit](https://replit.com/@fdasabino) IDE.

### Unfixed Bugs
1. I have commented out the code regarding the sound effects on lines 42, 43, 202, 210, 214, 217 on the [run.py](run.py) file.
The main reason being replit does not execute the pygame sound library.

<img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/commented_42%2C43.jpg">
<img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/commented_202%2C%20210%2C%20214%2C%20217.jpg">


2. When I run the application in my IDE the following warning appears in my command line:

[libpng warning: iCCP: known incorrect sRGB profile](https://www.google.com/search?q=libpng+warning%3A+iCCP%3A+known+incorrect+sRGB+profile&rlz=1C1CHBD_enSE943SE943&oq=libpng+warning%3A+iCCP%3A+known+incorrect+sRGB+profile&aqs=chrome.0.69i59.615j0j7&sourceid=chrome&ie=UTF-8)

3. When the application is stopped the following error is shown:

[pygame.error: video system not initialized](https://www.google.com/search?q=pygame.error%3A+video+system+not+initialized&rlz=1C1CHBD_enSE943SE943&sxsrf=ALeKk00M-Mu0KMq8QHLnGLyoLmtNzf8Vbg%3A1624296425479&ei=6cvQYP7YHKWQrgTq8KCQCw&oq=pygame.error%3A+video+system+not+initialized&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyAggAMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeUIaiAliGogJgv6QCaABwAngAgAF2iAHsAZIBAzAuMpgBAKABAqABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwi-8czbn6nxAhUliIsKHWo4CLIQ4dUDCA4&uact=5)

None of the above stops the program from running and executing, which makes me believe that
is a problem with some of pygame's libraries.

## Credits

### Libraries

1. The project was developed using [Pygame]()

### Media

1. Sound effects obtained from [Zapsplat](https://www.zapsplat.com).

2. The photos used on the home and sign up page are from [Pexels](https://www.pexels.com/).

3. The spaceship images were obtained from [NicePNG](NicePNG.com).
