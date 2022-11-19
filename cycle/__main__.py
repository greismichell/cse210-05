import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.score2 import Score2
from game.casting.player_one import PlayerOne
from game.casting.player_two import PlayerTwo
from game.casting.gems import Gem
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.control_actors_action_player2 import ControlActorsActionPlayer2
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("gems", Gem())
    cast.add_actor("playersOne", PlayerOne())
    cast.add_actor("playersTwo", PlayerTwo())
    cast.add_actor("scores", Score())
    cast.add_actor("scores2", Score2())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlActorsActionPlayer2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()