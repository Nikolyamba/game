import os

import arcade
from arcade import XYWH
from arcade.gui import UIGridLayout, UIAnchorLayout, UIFlatButton, UIView, UIManager

from windows.game_window import GameView

class MenuView(UIView):
    def __init__(self):
        super().__init__()

        self.ui = UIManager()
        self.ui.enable()

        grid = UIGridLayout(
        column_count=1,
        row_count=3,
        size_hint=(0, 0),
        vertical_spacing=10,
        horizontal_spacing=10,
        )

        self.ui.add(
            UIAnchorLayout(
                anchor_x="center_x",
                anchor_y="center_y",
                children=[grid]
            )
        )

        start_button = UIFlatButton(text="Старт игры", width=200)
        settings_button = UIFlatButton(text="Настройки", width=200)
        exit_button = UIFlatButton(text="Выход из игры", width=200)

        start_button.on_click = self.on_click_start
        exit_button.on_click = self.on_click_exit

        grid.add(start_button, row=0, column=0)
        grid.add(settings_button, row=1, column=0)
        grid.add(exit_button, row=2, column=0)

        self.background = arcade.load_texture("sprites/background.png")

    def on_show_view(self):
        self.ui.enable()

    def on_hide_view(self):
        self.ui.disable()

    def on_draw(self):
        self.clear()

        menu_rect = XYWH(
            x=self.window.width // 2,
            y=self.window.height // 2,
            width=self.window.width,
            height=self.window.height
        )

        arcade.draw_texture_rect(texture=self.background, rect=menu_rect)

        font_path = os.path.join("fonts", "bitmap.ttf")
        arcade.load_font(font_path)

        arcade.draw_text(
            "THE GAME",
            self.window.width // 2,
            self.window.height // 2 + 300,
            arcade.color.WHITE,
            font_size=48,
            font_name="Minecraft",
            anchor_x="center"
        )

        arcade.draw_text(
            "v0.1.2 alpha",
            30,
            50,
            arcade.color.GRAY,
            font_size=30,
            font_name="Minecraft"
        )

        self.ui.draw()


    def on_click_start(self, event):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

    def on_click_exit(self, event):
        arcade.close_window()