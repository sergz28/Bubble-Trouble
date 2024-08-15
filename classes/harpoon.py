from pyglet.math import Vec2
from pyglet import shapes



class Harpoon():

    def __init__(self, pos_x, pos_y, length=400, speed=500, batch=None):
        self.start_position = Vec2(pos_x, pos_y)
        self.current_length = 0
        self.max_length = length
        self.speed = speed
        self.extending = True  
        self.retracting = False
        self.shape = shapes.Line(pos_x, pos_y, pos_x, pos_y, width=2, color=(255, 255, 255), batch=batch)

    def check_collision(self, ball):
        AB = Vec2((self.shape.x2-self.shape.x), (self.shape.y2-self.shape.y))
        AP = Vec2((ball.position.x-self.shape.x),(ball.position.y-self.shape.y))
        t = (AP.dot(AB))/(AB.dot(AB))
        if t <= 0:
            cp = Vec2(self.shape.x, self.shape.y)
        elif t >= 1:
            cp = Vec2(self.shape.x2, self.shape.y2)
        elif 0 < t < 1:
            cp = Vec2((self.shape.x+t*(self.shape.x2-self.shape.x)),(self.shape.y + t * (self.shape.y2-self.shape.y)))

        dist = cp.distance(ball.position)
        if dist <= ball.radius:
            return True

    def update(self, dt):
        if self.extending:
            self.current_length += self.speed * dt
            if self.current_length >= self.max_length:
                self.current_length = self.max_length
                self.extending = False
                self.retracting = True
        elif self.retracting:
            self.current_length -= self.speed * dt
            if self.current_length <= 0:
                self.current_length = 0
                self.retracting = False  # 
         
        self.shape.y2 = self.start_position.y + self.current_length

    def is_finished(self):
        # Harpoon is finished when it has fully retracted
        return not self.extending and self.current_length <= 0