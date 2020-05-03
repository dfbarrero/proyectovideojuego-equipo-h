import math
import arcade
from random import randrange
from src.pcNpc.Bullet import Bullet
from src.pcNpc.LivingBeing import LivingBeing


class Player(LivingBeing):
    def __init__(self, position_x: int, position_y: int):
        """
        Creates an instance of the player (wielding a shotgun by default),
        although it contains the skin of every weapon.

        :param position_x: The initial x position of the player.
        :param position_y: The initial y position of the player.
        """

        super().__init__(position_x, position_y, "./resources/sprites/player/shotgun.png", 1)

        # Health
        self.health = 10

        # Skins
        self.append_texture(arcade.Texture("./resources/sprites/player/machinegun.png"))

        # Weapon
        self.weapon = "shotgun"
        self.shooting = False
        self.shotgun_sound = arcade.Sound("./resources/sounds/shotgun.wav")
        self.machinegun_sound = arcade.Sound("./resources/sounds/machinegun.wav")
        self.shoot_count = 0

        # Movement
        self.speed = 500
        self.mov_ud = ""
        self.mov_lr = ""

        # Bullseye
        self.bullseye = arcade.Sprite("./resources/sprites/player/bullseye.png", 0.75)
        self.mouse_position = [0, 0]

    def upd_orientation(self, x=None, y=None):
        x_ = self.bullseye.center_x - self.center_x
        y_ = self.bullseye.center_y - self.center_y
        length = math.sqrt(x_ ** 2 + y_ ** 2)
        if length == 0:
            length = 0.00001
        x_ /= length
        y_ /= length
        if y_ > 0:
            self.radians = math.acos(x_)
        else:
            self.radians = -math.acos(x_)

    def speed_up(self, delta_time):
        if self.mov_ud == "up":
            self.change_y = self.speed * delta_time
        elif self.mov_ud == "down":
            self.change_y = -self.speed * delta_time
        elif self.mov_ud == "":
            self.change_y = 0
        if self.mov_lr == "right":
            self.change_x = self.speed * delta_time
        elif self.mov_lr == "left":
            self.change_x = -self.speed * delta_time
        elif self.mov_lr == "":
            self.change_x = 0

    def draw(self):
        super().draw()
        self.bullseye.draw()

    def draw_debug(self):
        super().draw()
        super().draw_hit_box(arcade.color.GREEN, 1)
        self.bullseye.draw()

    def bullseye_pos(self, bottom_x, left_y):
        self.bullseye.center_x = self.mouse_position[0] + bottom_x
        self.bullseye.center_y = self.mouse_position[1] + left_y

    def shoot(self, delta_time: float, reloading: bool):
        """
        Creates the bullets shot by the player depending on the weapon he's wielding.

        :param reloading: Parameter to reload even if the player ain't shooting
        :param delta_time: To wait a fixed amount of time between shots (depending on the weapon).
        :return bullet_list: List of all the bullets created by the shot.
        """
        bullet_list = []

        if self.weapon == "shotgun":
            if self.shoot_count > 0:
                self.shoot_count -= 1 * delta_time
            elif self.shoot_count <= 0 and not reloading:
                self.shoot_count = 0.75
                for i in range(5):
                    rnd_angle = randrange(25)
                    angle = self.radians - math.pi / 6 + math.pi / 75 * rnd_angle
                    bullet = Bullet(0, 1000, 3, angle)
                    bullet_list.append(bullet)
                arcade.play_sound(self.shotgun_sound)
                self.shooting = False
        else:
            pass

        return bullet_list
