import arcade

from entities.player_settings import Player

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON
        self.player_list = None
        self.player_sprite = None

    def setup(self):
        self.player_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)

    def reset(self):
        """Reset the game to the initial state."""
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        self.player_list.draw()

    def on_update(self, delta_time : float = 1/60):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player_list.update(delta_time)

    def on_key_press(self, key, key_modifiers): #нажать клавишу что будет
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.ESCAPE:
            arcade.close_window()

        self.player_sprite.player_on_key_press(key)

    def on_key_release(self, key, key_modifiers): #отпустить клавишу что будет
        self.player_sprite.player_on_key_release(key)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass