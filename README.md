# Nasa vs Aliens - Spaceship Game

## Project Goals

- The main goal with this project is demonstrate the power of python programing language, and how simple it is to implement a
basic application concept.

- Nasa vs Aliens is a game developed to bring back the nostalgia of the 80s and 90s 2d games. This application target is mostly
people that enjoy a good, light old fashioned game to pass the time or simply for the act of socializing.

<img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/game_screen_shot%20-%20Copy.jpg">

## Features

### Existing Features


#### Health Status

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


#### 5 Bullets Rule

To make the game more exciting, players can only fire 5 bullets at the time. Players are not allowed to
fire again until their bullets are either off the screen or have hit the enemy ship.

<img src="">


#### Winner Text

Each time the opposite side reaches 0 health the winner is announced.

<img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/winner_text.jpg">


#### Features Left to Implement

1. In a near future I would like to implement a intro that presents the game.
2. Add a menu that let players choose their game character.


## Testing

[![Codeac](https://static.codeac.io/badges/2-377614318.svg "Codeac")](https://app.codeac.io/github/fdasabino/Project_python_mls3)


### Validator Testing

The code for this program was tested using the following:

The [PEP8 - validator](http://pep8online.com/) validator have shown some warnings with the code written, these warnings don't create any problems and were therefore ignored:

[PEP8 - Result File](https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Validating/PEP8.txt) containing the results and the code.


[Codeac - validator](https://app.codeac.io/github/fdasabino/Project_python_mls3)

<img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/checker2.jpg">


## Deployment

- The program has been published on [Replit](https://replit.com/@fdasabino/Projectpythonmls3?v=1).

- You can also find the files on my [Github](https://github.com/fdasabino/Project_python_mls3) repository.

## Unfixed Bugs

1. ### First bug:

I have commented out the code regarding the sound effects on lines 42, 43, 202, 210, 214, 217 on the [run.py](run.py) file on replit.
The main reason being replit does not execute the pygame sound library.

<img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/commented_42%2C43.jpg">
<img src="https://github.com/fdasabino/Project_python_mls3/blob/main/Assets/Screenshots/commented_202%2C%20210%2C%20214%2C%20217.jpg">

2. ### Second bug:

When the application executed the following error appears in my command line:

[libpng warning: iCCP: known incorrect sRGB profile](https://www.google.com/search?q=libpng+warning%3A+iCCP%3A+known+incorrect+sRGB+profile&rlz=1C1CHBD_enSE943SE943&oq=libpng+warning%3A+iCCP%3A+known+incorrect+sRGB+profile&aqs=chrome.0.69i59.615j0j7&sourceid=chrome&ie=UTF-8)


3. ### Third bug:

When the application is stopped the following error appears in my command line:

[pygame.error: video system not initialized](https://www.google.com/search?q=pygame.error%3A+video+system+not+initialized&rlz=1C1CHBD_enSE943SE943&sxsrf=ALeKk00M-Mu0KMq8QHLnGLyoLmtNzf8Vbg%3A1624296425479&ei=6cvQYP7YHKWQrgTq8KCQCw&oq=pygame.error%3A+video+system+not+initialized&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyAggAMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeUIaiAliGogJgv6QCaABwAngAgAF2iAHsAZIBAzAuMpgBAKABAqABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwi-8czbn6nxAhUliIsKHWo4CLIQ4dUDCA4&uact=5)

None of the above stops the program from running and executing, which makes me believe that is a problem with some of the pygame libraries.

## Credits

### Modules

1. The project was developed using [Pygame](https://www.pygame.org/news).

Pygame is a set of Python modules designed for writing video games. Pygame adds functionality
on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language.

Pygame is free. Released under the LGPL licence, you can create open source,
freeware, shareware, and commercial games with it. See the licence for full details.

### Media

1. Sound effects obtained from [Zapsplat](https://www.zapsplat.com).

2. The photos used on the home and sign up page are from [Pexels](https://www.pexels.com/).

3. The spaceship images were obtained from [NicePNG](NicePNG.com).

### Special Thanks

- A big thanks to Alan and the Student Support team for coming up with the deployment idea
and of course for their time.

- Thanks to Spencer my mentor for being so prompt and active when questions arise.