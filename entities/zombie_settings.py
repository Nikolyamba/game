import math
import random

from statemachine import State, StateMachine

import arcade

from features.settings import window_width, window_height

class ZombieState(StateMachine):
    CALM = State('Спокойствие', initial=True)
    WALKING = State('Ходьба')
    CHASE = State('Погоня')
    ATTACK = State('Атака')

    switch_to_walking = CALM.to(WALKING)
    switch_to_calm = WALKING.to(CALM)

class Zombie(arcade.Sprite):
    """ Player Class """
    def __init__(self, filename="sprites/z_right.png", scale=0.5):
        super().__init__(filename, scale)
        self.movement_speed = 2.5

        self.hp = 50

        self.state = ZombieState()
        self.state_timer = 0

        self.target_x = None
        self.target_y = None

        self.texture_right = arcade.load_texture("sprites/z_right.jpg")
        self.texture_left = arcade.load_texture("sprites/z_left.jpg")

    def get_x_y(self):
        self.target_x = random.randint(0, window_width)
        self.target_y = random.randint(0, window_height)

    def update_calm(self, delta_time):
        self.state_timer += delta_time

        if self.state_timer >= 15:
            self.state_timer = 0
            self.get_x_y()
            self.state = self.state.switch_to_walking()

    def update_walking(self, delta_time):
        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y

        distance = math.hypot(dx, dy)

        if distance < 5:
            self.change_x = 0
            self.change_y = 0
            self.state = self.state.switch_to_calm()
            return

        dx /= distance
        dy /= distance

        self.change_x = dx * self.movement_speed
        self.change_y = dy * self.movement_speed

    def update(self, delta_time):
        if self.state.current_state == ZombieState.CALM:
            self.update_calm(delta_time)
        elif self.state.current_state == ZombieState.WALKING:
            self.update_walking(delta_time)

        self.center_x += self.change_x
        self.center_y += self.change_y