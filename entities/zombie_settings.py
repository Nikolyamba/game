# import random
#
# import arcade
#
# from features.settings import window_width, window_height
#
# class Zombie(arcade.Sprite):
#     """ Player Class """
#
#     def __init__(self, filename="sprites/z_right.png", scale=0.5):
#         super().__init__(filename, scale)
#         self.movement_speed = 2.5
#
#         self.hp = 50
#
#         self.state = 'idle'
#
#         self.texture_right = arcade.load_texture("sprites/z_right.jpg")
#         self.texture_left = arcade.load_texture("sprites/z_left.jpg")
#
#     def zombie_move(self):
#         """Move logic"""
#         target_x = random.randint(-50, 50)
#         target_y = random.randint(-50, 50)
#         seconds = 45
#
#         if self.state == 'idle':
#             while seconds != 0:
#                 seconds -= 1
#             else:
#                 self.state = 'walking'
#         if self.state == 'walking':
#             if target_x >= 0:
#                 self.change_x += self.movement_speed
#             elif target_x < 0:
#                 self.change_x -= self.movement_speed
#             elif target_y >= 0:
#                 self.change_y += self.movement_speed
#             elif self.change_y < 0:
#                 self.change_y -= self.movement_speed
#
#     def update(self, delta_time: float = 1/60):
#         """ Move the zombie """
#         self.center_x += self.change_x
#         self.center_y += self.change_y
#
#         if self.left < 0:
#             self.left = 0
#         elif self.right > window_width - 1:
#             self.right = window_width - 1
#
#         if self.bottom < 0:
#             self.bottom = 0
#         elif self.top > window_height - 1:
#             self.top = window_height - 1