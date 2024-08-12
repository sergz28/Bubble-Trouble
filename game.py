import pyglet
from physics_engine.physics import *
from pyglet.window import key

# Creating a Window Object
window = pyglet.window.Window()
WIDTH = window.width
HEIGHT = window.height

# List for the ball objects
balls = []

# Graphics batch
batch = pyglet.graphics.Batch()


# Window events

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x,y, button, modifiers):
    for ball in balls:
        if ball.on_hit(x,y):
            ball.on_destroy(balls)
            break

@window.event
def on_key_press(symbol, modifiers):
    if (symbol == key.SPACE):
        new_ball = PhysicsObject(WIDTH/2, HEIGHT/2, 50, batch=batch)
        balls.append(new_ball)

def update(dt):
    for ball in balls:
        ball.apply_gravity(10)
        ball.check_collision(0, wall_b=WIDTH)
        ball.update(dt)

    
pyglet.clock.schedule_interval(update, 1/60)

pyglet.app.run()