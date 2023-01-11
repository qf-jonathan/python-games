from implementation.pygame import PygameEvent, PygameScreen, PygameTimer
from game import Game

if __name__=='__main__':
    screen = PygameScreen()
    timer = PygameTimer()
    event = PygameEvent()
    game = Game(screen=screen, timer=timer, event=event)
    game.run()
