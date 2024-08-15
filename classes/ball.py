from pyglet import shapes
from pyglet.math import Vec2
from physics_engine.physics import PhysicsObject


BALL_SIZES = {
    "extra_small": {"radius": 10, "bounce_height": 350},
    "small": {"radius": 20, "bounce_height": 450},
    "medium": {"radius": 40, "bounce_height": 550},
    "large": {"radius": 80, "bounce_height": 650}
}



class Ball(PhysicsObject):

    def __init__(self, pos_x, pos_y, size='medium', gravity=9.8, batch=None):
        super().__init__(pos_x, pos_y, gravity)
        size_info = BALL_SIZES[size]
        self.size = size
        self.radius = size_info['radius']
        self.bounce_height = size_info['bounce_height']
        
        self.batch = batch
        self.shape = shapes.Circle(pos_x, pos_y, self.radius, batch=batch)

    def update(self, dt):
        self.apply_gravity(self.gravity)
        self.update_physics(dt)

        self.shape.x = self.position.x
        self.shape.y = self.position.y

    def check_collision(self, floor_y, width):
        if self.position.y - self.radius <= floor_y:
            self.position.y = floor_y + self.radius
            self.velocity.y = self.bounce_height
        
        if self.position.x - self.radius <= 0:
            self.position.x = 0 + self.radius
            self.velocity.x = 200
        elif self.position.x + self.radius >= width:
            self.position.x = width - self.radius
            self.velocity.x = -200


    def destroy(self, balls):
        keys = list(BALL_SIZES.keys())
        for i, key in enumerate(keys):
            if self.size == 'extra_small':
                break

            if self.size == key:
                new_ball = Ball(self.position.x, self.position.y, keys[i-1], batch=self.batch)
                new_ball2 = Ball(self.position.x, self.position.y, keys[i-1], batch=self.batch)
                new_ball.velocity = Vec2(200, 50)
                new_ball2.velocity = Vec2(-200, 50)

                balls.append(new_ball)
                balls.append(new_ball2)
                break
            pass
        self.shape.delete()
        balls.remove(self)
        