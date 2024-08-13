from pyglet import shapes
import math


# 2D Vector Class
from pyglet import shapes
import math
class Vector2D():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x-other.x, self.y-other.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)   
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def length(self):
        return (self.x**2 + self.y**2)**0.5
    
    def normalize(self):
        length = self.length()
        if length != 0:
            return Vector2D(self.x / length, self.y / length)
        return Vector2D(0,0)
    


class PhysicsObject():

    def __init__(self, x, y, radius=0, mass=650, batch=None):
        self.position = Vector2D(x,y)
        self.velocity = Vector2D(0,0)
        self.radius = radius
        self.mass = mass
        self.batch = batch
        self.shape = shapes.Circle(x, y, radius, batch=batch)

    
    def apply_gravity(self, g, dt):
        self.velocity.y += -g

    def check_collision(self, ground_y, wall_a=0, wall_b=0):
        # Ground collision
        if self.position.y - self.radius <= ground_y:
            self.position.y = ground_y + self.radius
            self.velocity.y = 1 * self.mass
        # Wall collision
        # Left wall
        if self.position.x - self.radius <= wall_a:
            self.velocity.x *= -1
        elif self.position.x + self.radius >= wall_b:
            self.velocity.x *= -1

    def on_hit(self, x, y):
        dist = math.sqrt((self.position.x - x)**2 + (self.position.y - y)**2)
        return dist <= self.radius
    
    def on_destroy(self, balls):
        if self.radius <= 20:
            balls.remove(self)
        else:
            balls.remove(self)
            new_obj = PhysicsObject(self.position.x, self.position.y, self.radius - 20, mass=self.mass - 150, batch=self.batch)
            new_obj2 = PhysicsObject(self.position.x, self.position.y, self.radius - 20, mass=self.mass - 150, batch=self.batch)
            balls.append(new_obj)
            balls.append(new_obj2)
            # Horizontal Velocity
            new_obj.velocity += Vector2D(-200, 0)
            new_obj2.velocity += Vector2D(200, 0) 
            # Vertical Velocity
            new_obj.velocity += Vector2D(0, 250)
            new_obj2.velocity += Vector2D(0, 250)
            

    def update(self, dt):
        self.position += self.velocity * dt
        self.shape.x += self.velocity.x * dt
        self.shape.y += self.velocity.y * dt  