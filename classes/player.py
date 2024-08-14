from pyglet.math import Vec2
from pyglet import shapes
from pyglet.window import key

class Player():

    def __init__(self, pos_x, pos_y, batch=None):
        self.position = Vec2(pos_x, pos_y)
        self.velocity = Vec2(0.0,0.0)
        self.width = 21
        self.height = 50
        self.batch = None
        self.speed = 10
        self.shape = shapes.Rectangle(pos_x, pos_y, self.width, self.height, (255, 0, 191), batch=batch)
        

    def update(self, dt):
        self.position += self.velocity * dt
        self.shape.x = self.position.x
        self.shape.y = self.position.y  



    
    def check_collision(self, left, right, object=None):
        if self.position.x <= left:
            self.position.x = left + 1
            self.velocity.x = 0
            print(f'Collision at x-{left}')
        elif self.position.x + self.width >= right:  
            self.position.x = right - self.width - 1
            self.velocity.x = 0
            print(f'Collision at x-{right}')
    
    
    def move(self, direction):
        self.velocity = Vec2(direction * self.speed, 0) 