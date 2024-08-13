from physics_engine.physics import Vector2D
from pyglet import shapes
import math

class Player():
    def __init__(self, x,y, batch=None):
        self.position = Vector2D(x,y)
        self.velocity = Vector2D(0,0)
        self.batch = batch

        self.player_shape = shapes.Rectangle(x,y,20,60, batch=batch, color=(255,255,255,255))

    def move(self, direction, speed):
        self.velocity.x = direction * speed

    def update(self,dt):
        self.position += self.velocity * dt 
        self.player_shape.x += self.velocity.x * dt
        self.player_shape.y += self.velocity.y * dt
        
    def check_collision(self, left, right):
        if self.position.x <= left:
            return True
        elif self.position.x + self.player_shape.width >= right:
            return True
        else:
            return False
        


class Projectile():
    
    def __init__(self, x, y, width, height, batch=None):
        self.position = Vector2D(x,y)
        self.velocity = Vector2D(0,0)
        self.width = width
        self.height = height
        self.max_x = x+width
        self.max_y = y+height
        self.batch = batch
        self.hit = False
        self.shape = shapes.Rectangle(x, y, width, height, batch=batch)


    def shoot(self, dt):
        self.velocity = Vector2D(0, 100)
        self.shape.y += self.velocity.y * dt
        self.position += self.velocity * dt

    def check_collision(self, ball):
            px = max(self.position.x, min(ball.position.x, self.max_x))
            py = max(self.position.y, min(ball.position.y, self.max_y))

            dist = math.sqrt((px - ball.position.x)**2 + (py - ball.position.y)**2)

            return dist <= ball.radius
