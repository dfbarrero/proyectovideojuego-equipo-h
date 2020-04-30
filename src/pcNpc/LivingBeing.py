import math
import arcade
from random import randrange

class LivingBeing(arcade.Sprite):
    def __init__(self, position_x, position_y, image: str, scale: float):
        super().__init__(image, scale)
        self.alive = True
        self.health = None
        self.center_x = position_x
        self.center_y = position_y
        self.change_x = 0
        self.change_y = 0
        self.radians = 0

    def upd_orientation(self, x, y):
        x_ = x - self.center_x
        y_ = y - self.center_y
        length = math.sqrt(x_ ** 2 + y_ ** 2)
        x_ /= length
        y_ /= length
        if y_ > 0:
            self.radians = math.acos(x_)
        else:
            self.radians = -math.acos(x_)

    def damage(self):
        if self.alive:
            self.health -= 1
            if self.health <= 0:
                self.alive = False

    def revive(self):
        if not self.alive:
            self.alive = True
            self.health = 1