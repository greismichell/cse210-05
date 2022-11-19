import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_gems_collision1(cast)
            self._handle_gems_collision2(cast)
            self._handle_grow_player1_collision(cast)
            self._handle_grow_player2_collision(cast)
            self._handle_segment_collision1(cast)
            self._handle_segment_collision2(cast)
            self._handle_segment_collision3(cast)
            self._handle_segment_collision4(cast)
            self._handle_segment_collision1(cast)
            self._handle_game_over(cast)

    def _handle_gems_collision1(self, cast):
        """Updates the score if the player1 collides with the gem.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        gem = cast.get_first_actor("gems")
        player_one = cast.get_first_actor("playersOne")
        head = player_one.get_head()
       
        if head.get_position().equals(gem.get_position()):
            points = gem.get_points()
            player_one.grow_tail(points)
            score.add_points(points)
            gem.reset()
    
    def _handle_gems_collision2(self, cast):
        """Updates the score if the player2 collides with the gem.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score2 = cast.get_first_actor("scores")
        gem = cast.get_first_actor("gems")
        player_two = cast.get_first_actor("playersTwo")
        head2 = player_two.get_head()

        if head2.get_position().equals(gem.get_position()):
            points = gem.get_points()
            player_two.grow_tail(points)
            score2.add_points(points)
            gem.reset()
    

    def _handle_grow_player1_collision(self, cast):
        score = cast.get_first_actor("scores")
        player_one = cast.get_first_actor("playersOne")
        head = player_one.get_head()
        points1 = 0

        if head.get_position().equals(head.get_position()):
            points1 += 1
            player_one.grow_tail(points1)
            score.add_points(points1)

    def _handle_grow_player2_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        score2 = cast.get_first_actor("scores2")
        player_two = cast.get_first_actor("playersTwo")
        head2 = player_two.get_head()
        points2 = 0

        if head2.get_position().equals(head2.get_position()):
            points2 += 1
            player_two.grow_tail(points2)
            x = int(constants.MAX_X - 180)
            y = int(constants.MAX_Y - 595)
            position = Point(x, y)
            score2.add_points(points2)
            score2.set_position(position)
            


    def _handle_segment_collision1(self, cast):
        """Sets the game over flag if the palyer1 collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player_one = cast.get_first_actor("playersOne")
        head = player_one.get_segments()[0]
        segments = player_one.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()): 
            #or head.get_position().equals(segments2.get_position()) or head2.get_position().equals(segments.get_position()) :
                self._is_game_over = True


    def _handle_segment_collision2(self, cast):
        """Sets the game over flag if the player2 collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player_two = cast.get_first_actor("playersTwo")
        head2 = player_two.get_segments()[0]
        segments2 = player_two.get_segments()[1:]

        for segment in segments2:
            if head2.get_position().equals(segment.get_position()): 
                self._is_game_over = True

    def _handle_segment_collision3(self, cast):
        """Sets the game over flag if the head player1 collides with one of the segments of the player2.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player_one = cast.get_first_actor("playersOne")
        player_two = cast.get_first_actor("playersTwo")
        head = player_one.get_segments()[0]
        segments2 = player_two.get_segments()[1:]

        for segment in segments2:
            if head.get_position().equals(segment.get_position()): 
            #or head.get_position().equals(segments2.get_position()) or head2.get_position().equals(segments.get_position()) :
                self._is_game_over = True
            
    def _handle_segment_collision4(self, cast):
        """Sets the game over flag if the head player2 collides with one of the segments of the player1.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player_one = cast.get_first_actor("playersOne")
        player_two = cast.get_first_actor("playersTwo")
        segments = player_one.get_segments()[1:]
        head2 = player_two.get_segments()[0]
       

        for segment in segments:
            if head2.get_position().equals(segment.get_position()): 
            #or head.get_position().equals(segments2.get_position()) or head2.get_position().equals(segments.get_position()) :
                self._is_game_over = True
            
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player_one = cast.get_first_actor("playersOne")
            player_two = cast.get_first_actor("playersTwo")
            segments = player_one.get_segments()
            segments2 = player_two.get_segments()
            gem = cast.get_first_actor("gems")
           
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)    
            player_one.set_color(constants.WHITE)
            player_two.set_color(constants.WHITE)
            gem.set_color(constants.WHITE)