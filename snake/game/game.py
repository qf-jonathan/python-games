import sys
from game.objects import Snake, Food
from game.interfaces import Screen, Timer, Event


class Game:
    def __init__(self, screen: Screen, timer: Timer, event: Event):
        self.WINDOW_SIZE = 1000
        self.TILE_SIZE = 50
        self.screen = screen
        self.screen.set_size(self.WINDOW_SIZE)
        self.timer = timer
        self.event = event
        self.new_game()
        self.timer.set_frame_rate(60)
    
    def new_game(self):
        self.food = Food(self.screen, self.TILE_SIZE, self.WINDOW_SIZE)
        self.snake = Snake(self.screen, self.TILE_SIZE, self.WINDOW_SIZE, self.food, self.timer)

    def update(self):
        self.snake.update()
        if self.snake.check_borders() or self.snake.check_selfeating():
            self.new_game()
 
    def draw(self):
        self.screen.clear()
        self.screen.draw_scenary(self.TILE_SIZE)
        self.food.draw()
        self.snake.draw()
        self.screen.update()

    def check_event(self):
        self.event.load()
        if self.event.check(Event.QUIT):
            sys.exit()
        self.snake.control(self.event)
        self.event.clear()

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()
