import arcade

from features.settings import window_width, window_height

class Player(arcade.Sprite):
    """ Player Class """
    def __init__(self, filename="sprites/right.png", scale=0.5):
        super().__init__(filename, scale)
        self.movement_speed = 5

        self.texture_right = arcade.load_texture("sprites/right.png")
        self.texture_left = arcade.load_texture("sprites/left.png")

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