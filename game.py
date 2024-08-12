import pyglet
from random import randint
from physics_engine.physics import *
from pyglet.window import key
window = pyglet.window.Window(800, 600, 'Simple Physics test')


# List of ball objects
balls = []


# Creating gravity instance
gravity = Gravity(100)

# Ground constant
ground_y = 50

#Batch Object
batch = pyglet.graphics.Batch()

# FPS Display Object
fps_display = pyglet.window.FPSDisplay(window=window)


def on_death(balls, ball):
    for i in range(1,3):
        new_obj = PhysicsObject(ball.position.x, ball.position.y, ball.radius/2, batch=batch)
        
        if(i == 1):
            new_obj.velocity = Vector2D(-150,0)
        else:
            new_obj.velocity = Vector2D(150,0)

        balls.append(new_obj)
    balls.remove(ball)



if __name__ == '__main__':
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        for ball in balls:
            if ball.on_hit(x,y):
                on_death(balls,ball)
                break

    @window.event
    def on_key_press(symbol, modifiers):
        if(symbol == key.SPACE):
            new_ball = PhysicsObject(window.width/2, window.height/2, radius=20, mass=1, color=(randint(0,255), randint(0,255), randint(0,255), 255),batch=batch)
            balls.append(new_ball)


    @window.event
    def on_draw():
        window.clear()
        fps_display.draw()
        batch.draw()



    def update(dt):
        for ball in balls:
            gravity.apply(ball)
            ball.update(dt)
            check_collision(ball, ground_y, 0, window.width)
        

    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()


