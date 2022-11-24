> cse210-05-Cycle Game 
# Cycle Game: 
 - [Porpuse](http://github.com/greismichell/cse210-04/blob/main/README.md#Porpuse)
 - [Game Specificatiom](https://github.com/greismichell/cse210-04/blob/main/README.md#Game-Specification)
 - [Game Design](https://github.com/greismichell/cse210-04/blob/main/README.md#Game-Design)
 - [Project Structure](https://github.com/greismichell/cse210-04/blob/main/README.md#Project-Structure)
 - [Getting Started](https://github.com/greismichell/cse210-04/blob/main/README.md#Getting-Started)
 - [Required Technologies](https://github.com/greismichell/cse210-04/blob/main/README.md#Required-Technologies)
 - [Autors](https://github.com/greismichell/cse210-04/blob/main/README.md#Autors)

## Porpuse
---
Develop and demostrate the mastery of the:
- Design software using the principales of programing with classes (abstraction, encapsulation, inheritance and polymorphism)
  - Design a program using the principle of polymorphism.

## Game Specification
---
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

 ### Cycle Rules
 
   Cycle is played according to the following rules:

   * Players can move up, down, left and right...
       * Player one moves using the W(up), S(down), A(left) and D(right) keys.
       * Player two moves using the I(up), K(down), J(left) and L(right) keys.
       * There are gems that need to be catch and each of them apper randomly around the screen and with values in range 1 to 8 in different colors.

   * Each player's trail grows as they move and catch gems.
   * Players try to maneuver so the opponent collides with their trail.
   * If a player collides with their opponent's trail...
       * A "game over" message is displayed in the middle of the screen.
       * The cycles turn white.
       * Players keep moving and turning but don't run into each other.


## Game Design
---
```
* Object: Director:
    "A person who directs the game."
 
    Responsibility:
    - Control the sequence of play.

    Behaviors:
    - Create a new match game using the keyboard and video services, and optain the score.

    State: 

    - Start_game:  Starts the game using the given cast. Runs the main game loop.
    - execute_actions: Calls execute for each action in the given group.


* Object: Actor:
    "A visible, moveable thing that participates in the game."

    Responsibility:  
    - Keep track of its appearance, position and velocity in 2d space, and its value.

    Behavior: 
    - Construct news artifacts.

    State: 
    - get_color: Gets the actor's color as a tuple of three ints (r, g, b).
    - get_font_size: Gets the actor's font size.
    - get_position: Gets the artifact's position in 2d space.
    - get_value(int): get the value of each artifact.
    - get_text: Gets the actor's textual representation.
    - get_velocity: Gets the actor's speed and direction.
    - move_next: Moves the artifact to its next position according to its velocity. Will wrap the position from one side of the screen to the other when it reaches the given maximum x and y values.
    - set_color: Updates the color to the given one.
    - set_position: Updates the position to the given one.
    - set_font_size: Updates the font size to the given one.
    - set_text: updates the text to the given one.
    -set_velocity: Updates the velocity to the given one.


* Object: Player One:
    " The player in the right position "

    Responsability: 
    -  The responsibility of player one  is to move itself.

    States:
    - get_segments: get the segments 
    - get_head: obtain the position of the head.
    - grow_tail: enlarge the body as he move:
    - turn_head: move head.
    - prepare_ body: position the body in the corret place at the begining.


* Object: Player Two:
    " The player in the left position"

    Responsability: 
    -  The responsibility of player two is to move itself.

    States:
    - get_segments: get the segments 
    - get_head: obtain the position of the head.
    - grow_tail: enlarge the body as he move:
    - turn_head: move head.
    - prepare_ body: position the body in the corret place at the begining.


* Object: Score:
    "A record of points made"

    Responsibility:
    - to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string representation of the points earned.

    Behavior: 
   - get the points and save them

    State:
    - add_points: Adds the given points to the score's total points.


* Object: Action: 
    "A thing that is done."
     
    Responsibility:
    - The responsibility of action is to do somthing that is integral or important in the game. Thus, it has one method, execute(), which should be overridden by derived classes.

    States:
    - execute: Executes something that is important in the game. This method should be overriden by 
        derived classes.


* Object: Control Player One Actions(Action) :
    "An input action that controls the player one by using inheritance to the Action class."

    Responsibility:
    - The responsibility is to get the direction and move the player's head

   Behavior: Constructs a new Control Player One Action using the specified KeyboardService.

    States:
    - Execute: Use the method "execute" finded in the action class and chance its behavior by applaying polymorphism.


* Object: Control Player Two Actions(Action) :
    "An input action that controls the player two by using inheritance to the Action class."

    Responsibility:
    - The responsibility is to get the direction and move the player's head

   Behavior: Constructs a new Control Player One Action using the specified KeyboardService.

    States:
    - Execute: Use the method "execute" finded in the action class and chance its behavior by applaying polymorphism.


*  Object: Draw Actors Action(Action):
    "An output action that draws all the actors by using polymoorphism"

    Responsability: 
    - The responsibility of DrawActorsAction is to draw all the actors.

    States:
    execute:  Executes the draw actors action by applaying polymorphism.


* Object Handle Collisions Action: 
   "An update action that handles interactions between the actors."  

   Responsibility:
   - The responsibility of Handle Collisions Action is to handle the situation when the snake collides with the player collides of the second player segments and the game is over.  

   States: 
   - execute: using polymorphism Executes the handle collisions action.
   - handle_segment_collision: Sets the game over flag if the player collides with one of the second player segments.
   - handle_game_over: Shows the 'game over' message and turns the players's bodies and head white if the game is over.


* Object: Move Actors Action (Action):
    "keep track of the movements of the players."

    Responsability: 
    - Override the execute(cast, script) method

    States: 
    - execute: Using polymorphism get all the actors from the cast, loop throug, the actors and call the move_next() method on each actor


* Object: Script: 
    "A collection of actions."

    Responsinility: 
    - The responsibility of Script is to keep track of a collection of actions. It has methods for adding, removing and getting them by a group name.

    States:
    - add_actions: Adds an action to the given group.
    - get_actions: Gets the actions in the given group.
    - remove_actions: Removes an action from the given group.


* Object: Cast:
    "A collection of artifacts."

    Responsibility:
    - keep track of a collection of artifacts. It has methods for adding, removing and getting them by a group name.

    Behavior:  
    - A dictionary of actors { key: group_name, value: a list of  artifacts}

    States:

    - Add_artifact: adss an artifact to the given group.
    - Get_artifacts: get the artifacts in the given group.
    - Get_ all_ the_artifacts: gets all the artifacts in the cast.
    - Get_first_artifact: gets the first artifact in the given group.
    - Remove_artifact: removes an artifact from the given group.


* Object: KeyboardService:
    "Detects player input."
   
    Responsibility:
    - Dectect player key presses and translate them into a point representing a direction.

    Behavior:
    - Scalling directional intput to a grip.
   States:
    - Get_ direction: gets the slected direction based on the currently pressed keys.
                  

* Object: Video Service:
    "Outputs the game state"

    Responsibility: 
    - The responsibility of the class of objects is to draw the game state on the screen.

    Behaviors:
    - Debug (bool): wheter or not to draw in debug mode.

    States:

    - Clase_window: Closes the window and releases all computing resources.
    - Clear_buffer: Clears the buffer in preparation for the next rendering. This method   should be called at the beginning of the game's output phase.
    - Draw_artifact: Draws the given artifact's text on the screen.
    - Draw_artifacs: Draws the text for the given list of artifacts on the screen.
    - Flush_buffer: Copies the buffer contents to the screen. This method should be called at the end of  the game's output phase.
    - Get_cell_size: Gets the video screen's cell size.
    - Get_height: Gets the video screen's height.
    - Get_width: Gets the video screen's width.
    - Is_window_open: Whether or not the window was closed by the user.
    - Open_window: Opens a new window with the provided title.
    - Draw_grid: Draws a grid on the screen.


* Object: Color:
    "A color"

    Responsibility:
    - Hold and provide information about itself. Color has a few convenience methods for comparing them and converting to a tuple.

    Behaviors:
    - Put color through:
        - red (int): The red value.
        - green (int): The green value.
        - blue (int): The blue value.
        - alpha (int): The alpha or opacity.

    Staste:
    - To_tuple: Gets the color as a tuple of four values (red, green, blue, alpha).


* Object: Point:
    "A distance from a relative origin (0, 0)."

    Responsinility:
    - Hold and provide information about itself. Point has a few convenience methods for adding, scaling, and comparing them.

    Behaviors:
    - Constructs a new Point using the specified x and y values.

    State:

    - Add:  Gets a new point that is the sum of this and the given one.
    - Equals: Whether or not this Point is equal to the given one.
    - Get_x: "Gets the horizontal distance.
    - Get_y: Gets the vertical distance.
    - Scale: Scales the point by the provided factor.
```

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cycle                (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cycle
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Autors
---
- Greis Michell Garcia Villanueva