from random import randrange
from game.interfaces import Screen, Timer, Event


class Snake:
    def __init__(self, screen: Screen, size: int, window_size: int, food: 'Food', timer: Timer):
        self.screen = screen
        self.size = size
        self.window_size = window_size
        self.food = food
        self.timer = timer
        self.position = self.get_random_position()
        self.direction = (0, 0)
        self.step_delay = 100
        self.time = 0
        self.length = 1
        self.segments = []
    
    def control(self, event: Event):
        if event.check('up') and (self.direction[1] == 0 or self.length == 1):
            self.direction = (0, -self.size)
        if event.check('down') and (self.direction[1] == 0 or self.length == 1):
            self.direction = (0, self.size)
        if event.check('left') and (self.direction[0] == 0 or self.length == 1):
            self.direction = (-self.size, 0)
        if event.check('right') and (self.direction[0] == 0 or self.length == 1):
                self.direction = (self.size, 0)

    def delta_time(self):
        now = self.timer.get_current()
        if now - self.time > self.step_delay:
            self.time = now
            return True
        return False

    def get_random_position(self):
        return (randrange(self.size, self.window_size - self.size, self.size),) * 2

    def check_borders(self):
        if self.position[0] < 0 or self.position[0] + self.size > self.window_size:
            return True
        if self.position[1] < 0 or self.position[1] + self.size > self.window_size:
            return True
        return False
        
    def check_food(self):
        if self.position == self.food.position:
            self.food.position = self.get_random_position() # need a refactor, it should not be called here
            self.length += 1
        
    def check_selfeating(self):
        return len(self.segments) != len(set(self.segments))

    def move(self):
        if self.delta_time():
            self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
            self.segments.append(self.position)
            self.segments = self.segments[-self.length:]

    def update(self):
        self.check_selfeating()
        self.check_food()
        self.move()

    def draw(self):
        for segment in self.segments:
            self.screen.draw_square('green', segment, self.size)


class Food:
    def __init__(self, screen: Screen, size: int, window_size: int):
        self.screen = screen
        self.size = size
        self.window_size = window_size
        self.position = self.get_random_position()
    
    def get_random_position(self):
        return (randrange(self.size, self.window_size - self.size, self.size),) * 2

    def draw(self):
        self.screen.draw_square('red', self.position, self.size)
