import numpy as np

class Character:
    def __init__(self):
        self.appearance = 'circle'
        self.state = 'run' # slide, jump
        self.outline = '#FF0000'
        self.speed = 3
        self.jump_power = 10
        self.gravity = 1
        self.velocity = 0
        self.jump_count = 2
        self.on_ground = False
        self.position = np.array([30, 150, 60, 210])
        # 캐릭터 중앙 점
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

    def replace(self):
        self.position = np.array([30, self.position[1] - 30, 60, self.position[3]])

    def jump(self):
        
        if self.jump_count > 0:
            if self.state == 'slide':
                self.position = np.array([30, self.position[1] - 30, 60, self.position[3]])
            self.velocity = -self.jump_power
            self.state = 'jump'
            self.jump_count -= 1
        

    def slide(self):
        if (self.state != 'jump' and self.on_ground):
            self.state = 'slide'
            self.position = np.array([30, 180, 60, 210])

    def move(self):
            
        if not self.on_ground:
            self.state == 'jump'

            
        self.position[1] += self.velocity
        self.position[3] += self.velocity
        self.velocity += 1
                
        #center update
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2]) 