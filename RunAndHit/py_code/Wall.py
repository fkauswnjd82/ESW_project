import numpy as np

class Wall:
    def __init__(self, spawn_position, num):
        self.is_out = False
        self.state = 'wall'
        self.outline = "#FF0000"
        if (num == 1):
            self.position = np.array([spawn_position[0] + 10, spawn_position[1], spawn_position[0] + 20, spawn_position[1] + 165])
            self.state = 'wall'
        elif (num == 2):
            self.position = np.array([spawn_position[0] + 10, spawn_position[1] + 10, spawn_position[0] + 20, spawn_position[1] + 20])
            self.state = 'fireball'
    
    def move(self, speed):
        self.position -= np.array([speed, 0, speed, 0])

    def collision_check(self, other):
        
        collision = self.overlap(self.position, other.position)

        if collision:
            other.speed = 0
            other.velocity = 0
            other.gravity = 0
            other.speed = 0
            other.jump_count = 0
            other.state = 'die'


    def overlap(self, rect1, rect2):
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[1] > rect2[3] or rect1[3] < rect2[1])