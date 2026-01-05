import arcade

from features.settings import window_height, window_width
from windows.game_window import GameView

window_title = 'TheGame'

def main():
    """ Main function """
    window = arcade.Window(window_width, window_height, window_title)

    game = GameView()
    game.setup()
    window.show_view(game)

    arcade.run()

if __name__ == "__main__":
    main()