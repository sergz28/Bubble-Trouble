import pyglet
from random import randint
from physics_engine.physics import Vector2D, PhysicsObject, Gravity, check_collision

window = pyglet.window.Window(800, 600, 'Simple Physics test')


# List of balls
balls = []


# Creating gravity instance
gravity = Gravity(g=30)


ground_y = 50


@window.event
def on_mouse_press(x, y, button, modifiers):
    new_ball = PhysicsObject(x, y, radius=20, mass=1, color=(randint(0,255), randint(0,255), randint(0,255), 255))
    balls.append(new_ball)


fps_display = pyglet.window.FPSDisplay(window=window)

@window.event
def on_draw():
    window.clear()
    fps_display.draw()
    for ball in balls:
        pyglet.shapes.Circle(int(ball.position.x), int(ball.position.y),
                              ball.radius, color=ball.color).draw()





def update(dt):
    for ball in balls:
        gravity.apply(ball)
        ball.update(dt)
        check_collision(ball, ground_y)
    

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()