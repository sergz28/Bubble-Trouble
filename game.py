import pyglet
from physics_engine.physics import *
from pyglet.window import key
from classes.player import Player, Projectile
from pyglet.window import mouse
# Creating a Window Object
window = pyglet.window.Window()
WIDTH = window.width
HEIGHT = window.height

# List for the ball objects
balls = []

projectile = None

# Graphics batch
batch = pyglet.graphics.Batch()

# Make player
player = Player(WIDTH/2, 0, batch=batch)


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
    global projectile
    if (symbol == key.SPACE):
        new_ball = PhysicsObject(WIDTH/2, HEIGHT/2, 50, batch=batch)
        balls.append(new_ball)
    
    if (symbol == key.LEFT):
        player.move(-1, 300)
    if (symbol == key.RIGHT):
        player.move(1, 300)

    if (symbol == key.UP):
        projectile = Projectile(player.position.x+player.player_shape.width/2, player.position.y-1000, 5, 1000, batch=batch)


    

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT:
        player.velocity = Vector2D(0,0)
    if symbol == key.RIGHT:
        player.velocity = Vector2D(0,0)


def update(dt):
    global projectile
    if projectile is not None:
        projectile.shoot(dt)
        for ball in balls:
            if projectile.check_collision(ball):
                ball.on_destroy(balls)
                break
                

    if not player.check_collision(0, WIDTH):
        player.update(dt)
    else:
        player.velocity.x *= -1
        player.update(dt)
    for ball in balls:
        ball.apply_gravity(10, dt)
        ball.check_collision(0, wall_b=WIDTH)
        ball.update(dt)
    

    
pyglet.clock.schedule_interval(update, 1/60)

pyglet.app.run()