import arcade

from features.settings import window_width, window_height

class Player(arcade.Sprite):
    """ Player Class """
    def __init__(self, filename="sprites/right.png", scale=0.5):
        super().__init__(filename, scale)
        self.movement_speed = 5
        self.center_x = 50
        self.center_y = 50

        self.texture_right = arcade.load_texture("sprites/right.png")
        self.texture_left = arcade.load_texture("sprites/left.png")

    def player_on_key_press(self, key):
        if key == arcade.key.W:
            self.change_y = self.movement_speed
        elif key == arcade.key.S:
            self.change_y = -self.movement_speed
        elif key == arcade.key.A:
            self.change_x = -self.movement_speed
            self.texture = self.texture_left
        elif key == arcade.key.D:
            self.change_x = self.movement_speed
            self.texture = self.texture_right

    def player_on_key_release(self, key):
        if key == arcade.key.W or key == arcade.key.S:
            self.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.change_x = 0

    def update(self, delta_time: float = 1/60):
        """ Move the player """
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > window_width - 1:
            self.right = window_width - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > window_height - 1:
            self.top = window_height - 1

