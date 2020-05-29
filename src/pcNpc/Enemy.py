import math
from src.pcNpc.LivingBeing import LivingBeing


class Enemy(LivingBeing):
    def __init__(self, position_x: int, position_y: int, type_: int):
        self.type = type_
        if type_ == 0:  # Blue enemy
            super().__init__(position_x, position_y, "./resources/sprites/enemies/blueZombie.png", 1)
            self.speed = 400
        elif type_ == 1:  # Orange enemy
            super().__init__(position_x, position_y, "./resources/sprites/enemies/orangeZombie.png", 2)
            self.speed = 500

    def go_to(self, x, y):
        dx = self.center_x - x
        dy = self.center_y - y
        d = math.sqrt(dx ** 2 + dy ** 2)
        if d == 0:
            d = 0.0001

        if self.image == "./resources/sprites/enemies/blueZombie.png":
            self.change_x = -self.speed / d * dx
            self.change_y = -self.speed / d * dy

        elif self.image == "./resources/sprites/enemies/orangeZombie.png":
            self.change_x = -self.speed * 1.5 / d * dx
            self.change_y = -self.speed * 1.2 / d * dy

    def draw_debug(self):
        self.draw()
        self.draw_hit_box()
