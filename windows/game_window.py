import arcade
from arcade import XYWH

from entities.player_settings import Player
from features.settings import window_height
from features.timer import Time


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON

        self.player_list = None
        self.player_sprite = None

        self.timer = Time()
        self.timer.start()

    def setup(self):
        self.player_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)

        self.health_texture = arcade.load_texture("sprites/health.png")
        self.stamina_texture = arcade.load_texture("sprites/stamina.png")

    def reset(self):
        """Reset the game to the initial state."""
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        self.player_list.draw()

        heart_rect = XYWH(x=30, y=window_height-30, width=120, height=60)
        stamina_rect = XYWH(x=30, y=window_height-90, width=60, height=60)

        arcade.draw_texture_rect(texture=self.health_texture, rect=heart_rect)
        arcade.draw_text(str(self.player_sprite.hp), x=70, y=window_height-40, font_name="Minecraft", font_size=20)

        arcade.draw_texture_rect(texture=self.stamina_texture, rect=stamina_rect)
        arcade.draw_text(str(self.player_sprite.stamina), x=70, y=window_height-90, font_name="Minecraft", font_size=20)

        seconds, minutes, hours = self.timer.get_sec_min_hrs(self.timer.time_passed())

        arcade.draw_text(
            f"{hours}:{minutes}:{seconds}",
            x = self.window.width // 2,
            y = self.window.height // 2 + 450,
            font_size=40,
            font_name="Minecraft",
            color=arcade.color.WHITE,
            anchor_x="center"
        )

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

    # def on_mouse_motion(self, x, y, delta_x, delta_y):
    #     pass
    #
    # def on_mouse_press(self, x, y, button, key_modifiers):
    #     pass
    #
    # def on_mouse_release(self, x, y, button, key_modifiers):
    #     pass