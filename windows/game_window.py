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
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
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

        if key == arcade.key.W:
            self.player_sprite.change_y = self.player_sprite.movement_speed
        elif key == arcade.key.S:
            self.player_sprite.change_y = -self.player_sprite.movement_speed
        elif key == arcade.key.A:
            self.player_sprite.change_x = -self.player_sprite.movement_speed
        elif key == arcade.key.D:
            self.player_sprite.change_x = self.player_sprite.movement_speed

    def on_key_release(self, key, key_modifiers): #отпустить клавишу что будет
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass