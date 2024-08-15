from pyglet.math import Vec2
from pyglet import shapes
from pyglet.window import key
from classes.harpoon import Harpoon
class Player():

    def __init__(self, pos_x, pos_y, batch=None):
        self.position = Vec2(pos_x, pos_y)
        self.velocity = Vec2(0.0,0.0)
        self.width = 21
        self.height = 50
        self.batch = batch
        self.speed = 10
        self.shape = shapes.Rectangle(pos_x, pos_y, self.width, self.height, (255, 0, 191), batch=batch)
        self.harpoon = None


    def deploy_harpoon(self):
        if self.harpoon is None or self.harpoon.is_finished():
            self.harpoon = Harpoon(self.position.x+self.width/2, self.position.y, batch=self.batch)
    

    def update(self, dt):
        self.position += self.velocity * dt
        self.shape.x = self.position.x
        self.shape.y = self.position.y  

        if self.harpoon:
            self.harpoon.update(dt)
            if self.harpoon.is_finished():
                self.harpoon = None



    
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

    