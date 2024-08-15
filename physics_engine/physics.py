from pyglet.math import Vec2

class PhysicsObject():
    def __init__(self, pos_x, pos_y, gravity=9.81, radius=None):
        self.position = Vec2(pos_x, pos_y)
        self.velocity = Vec2(0, 0)
        self.gravity = gravity

    
    def apply_gravity(self, gravity):
       self.velocity.y += -gravity


    def update_physics(self,dt):
        self.position += self.velocity * dt
  


