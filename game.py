import pyglet
from classes.player import Player
from pyglet.window import key
from pyglet.math import Vec2
from classes.ball import Ball, BALL_SIZES
from classes.harpoon import Harpoon
win = pyglet.window.Window()
batch = pyglet.graphics.Batch()

# Initialising game variables

# Player
player = Player(win.width/2, win.height * 0.1, batch=batch)
player.speed = 300
last_input = False
# Balls

ball_large = Ball(win.width/2, win.height - 50, size="large", batch=batch)
# ball_medium = Ball(win.width/3, win.height - 50, size="medium", batch=batch)
# ball_small = Ball(win.width/4, win.height - 50, size="small", batch=batch)
# ball_extra_small = Ball(win.width/5, win.height - 50, size="extra_small", batch=batch)

balls = [ball_large]

if __name__ == '__main__':
    @win.event
    def on_draw():
        win.clear()
        batch.draw()

    @win.event
    def on_key_press(symbol, modifiers):
        global last_input
        # Player Movement Handling
        match symbol:
            case key.A | key.LEFT:
                    player.move(-1)
                    last_input = False
            case key.D | key.RIGHT:
                    player.move(1)
                    last_input = True
            case key.SPACE:
                  player.deploy_harpoon()
    @win.event
    def on_key_release(symbol, modifiers):
        
        # Player Movement, must make velocity 0 once key is released
        match symbol:
            case key.A | key.LEFT:
                if not last_input:
                    player.velocity = Vec2(0,0)
            case key.D | key.RIGHT:
                if last_input:
                    player.velocity = Vec2(0,0)

    def update(dt):
        player.check_collision(0, win.width)
        player.update(dt)
        for ball in balls:
             ball.update(dt)
             ball.check_collision(win.height * 0.1, win.width)

        for ball in balls:
             if player.harpoon:
               if player.harpoon.check_collision(ball):
                    ball.destroy(balls)
                    player.harpoon = None
                    break
    
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()