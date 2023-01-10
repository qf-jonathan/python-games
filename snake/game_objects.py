import pygame as pg
from random import randrange

vec2 = pg.math.Vector2

class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, self.size - 2, self.size - 2])
        self.rect.center = self.get_random_position()
        self.direction = vec2(0, 0)
        self.step_delay = 100
        self.time = 0
        self.length = 1
        self.segments = []
    
    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in [pg.K_w, pg.K_UP] and (self.direction.y == 0 or self.length == 1):
                self.direction = vec2(0, -self.size)
            if event.key in [pg.K_s, pg.K_DOWN] and (self.direction.y == 0 or self.length == 1):
                self.direction = vec2(0, self.size)
            if event.key in [pg.K_a, pg.K_LEFT] and (self.direction.x == 0 or self.length == 1):
                self.direction = vec2(-self.size, 0)
            if event.key in [pg.K_d, pg.K_RIGHT] and (self.direction.x == 0 or self.length == 1):
                self.direction = vec2(self.size, 0)

    
    def delta_time(self):
        now = pg.time.get_ticks()
        if now - self.time > self.step_delay:
            self.time = now
            return True
        return False

    def get_random_position(self):
        return [randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)] * 2

    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_SIZE:
            self.game.new_game()
        
    def check_food(self):
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position() # need a refactor, it should not be called here
            self.length += 1
        
    def check_selfeating(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]

    def update(self):
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.move()

    def draw(self):
        for segment in self.segments:
            pg.draw.rect(self.game.screen, 'green', segment)


class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, self.size - 2, self.size - 2])
        self.rect.center = self.get_random_position()
    
    def get_random_position(self):
        return [randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)] * 2

    def update(self):
        pass

    def draw(self):
        pg.draw.rect(self.game.screen, 'red', self.rect)
