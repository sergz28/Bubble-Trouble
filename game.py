import pyglet
from classes.player import Player
from pyglet.window import key
from pyglet.math import Vec2
win = pyglet.window.Window()
batch = pyglet.graphics.Batch()

# Initialising game variables

# Player
player = Player(win.width/2, win.height * 0.1, batch=batch)
player.speed = 300


if __name__ == '__main__':
    @win.event
    def on_draw():
        win.clear()
        batch.draw()

    @win.event
    def on_key_press(symbol, modifiers):
        # Player Movement Handling
        match symbol:
            case key.A:
                    player.move(-1)
            case key.D:
                    player.move(1)
    @win.event
    def on_key_release(symbol, modifiers):
        # Player Movement, must make velocity 0 once key is released
        match symbol:
            case key.A:
                player.velocity = Vec2(0,0)
            case key.D:
                player.velocity = Vec2(0,0)

    def update(dt):
        player.check_collision(0, win.width)
        player.update(dt)

    

    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()