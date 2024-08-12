from pyglet import shapes
import math
class Vector2D():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __str__(self):
        return f'({self.x}, {self.y})'


    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def length(self):
        return (self.x**2 + self.y**2)**0.5
    
    def normalize(self):
        length = self.length()
        if length != 0:
            return Vector2D(self.x/length, self.y/length)
        
        return Vector2D(0, 0)
    
class PhysicsObject():
    def __init__(self, x, y, radius, mass=1.0, color=(255,255,255,255), batch=None):
        self.position = Vector2D(x,y)
        self.velocity = Vector2D(0,0)
        self.radius = radius
        self.mass = mass
        self.restitution = 0.9
        self.color = color

        self.shape = shapes.Circle(x,y,radius,color=color, batch=batch)
    
    def apply_force(self, force):
        acceleration = Vector2D(force.x * self.mass, force.y * self.mass)

        self.velocity += acceleration

    def update(self, dt):
        self.position += self.velocity * dt

        self.shape.x = self.position.x
        self.shape.y = self.position.y
    
    def on_hit(self, x, y):
        dist = math.sqrt((self.position.x - x)**2 + (self.position.y - y)**2)
        return dist <= self.radius
        

    

class Gravity():
    def __init__(self, g=9.8):
        self.gravity = Vector2D(0, -g)
    def apply(self, obj):
        obj.apply_force(self.gravity)

    

def check_collision(obj, ground_y, x_left, x_right):
    if obj.position.y - obj.radius < ground_y:
        obj.position.y = ground_y + obj.radius
        obj.velocity.y *= -1
    if obj.position.x - obj.radius <= x_left:
        obj.position.x = 0 + obj.radius
        obj.velocity.x *= -1
    if obj.position.x + obj.radius >= x_right:
        obj.position.x = x_right - obj.radius
        obj.velocity.x *= -1


