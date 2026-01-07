import arcade

from features.settings import window_height, window_width
from windows.game_window import GameView
from windows.menu_window import MenuView

window_title = 'TheGame'

def main():
    """ Main function """
    window = arcade.Window(window_width, window_height, window_title)

    menuView = MenuView()
    window.show_view(menuView)

    arcade.run()

if __name__ == "__main__":
    main()