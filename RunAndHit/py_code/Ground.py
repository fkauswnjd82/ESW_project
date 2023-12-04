import numpy as np
from Wall import Wall
from Thron import Thron
from Joystick import Joystick


joystick = Joystick()

class Ground:
    def __init__(self, spawn_position, num):
        
        self.appearance = 'rectangle'
        self.is_out = False
        self.state = 'ground'
        self.outline = "#FF0000"
        if (num == 1): # 땅
            self.state = 'ground'
            self.position = np.array([spawn_position[0], spawn_position[1], spawn_position[0] + 30, spawn_position[1] + 30])
        elif (num == 2): # 플렛폼
            self.state = 'platform'
            self.position = np.array([spawn_position[0], spawn_position[1], spawn_position[0] + 30, spawn_position[1] + 10])
        elif (num == 3): # 마지막 땅 위치
            self.state = 'lastPos'
            self.outline = '#00FF00'
            self.position = np.array([spawn_position[0], spawn_position[1], spawn_position[0] + 30, spawn_position[1] + 30])

    # 맵 찍는 함수
    def makeMaps(grounds, walls, throns, num = 0):

        startPos = 240
        startPlatPos = 8
        if num == 0:
            startPos = 0
            startPlatPos = 0
        # 함수 내부에서 쓸 함수 정의
        def makeOneGround(pos):
            grounds.append(Ground((startPos + int(30 * (pos - 1)), 210), 1))
            
        def makeOnePlatform(pos):
            grounds.append(Ground((startPos + int(30 * (pos - 1)), 180 + int(10 * (pos - 3 + startPlatPos))), 2))

        def makelastPos(pos):
            grounds.append(Ground((startPos + int(30 * (pos - 1)), 120), 3))

        def makeOneWall(pos):
            walls.append(Wall((startPos + int(30 * (pos - 1)), 0), 1))

        def makeOneFireball(pos, hPos):
            walls.append(Wall((startPos + int(30 * (pos - 1)), 210 - int((hPos * 30))), 2))

        def makeOneThron(pos, num):
            throns.append(Thron((startPos + int(30 * (pos - 1)), 210), num))

        if num == 0:
            # 시작 지형 8개
            makeOneGround(1)
            makeOneGround(2)
            makeOneGround(3)
            makeOneGround(4)
            makeOneGround(5)
            makeOneGround(6)
            makeOneGround(7) 
            makeOneGround(8); makelastPos(8)

        elif num == 1:
            makeOneGround(1)
            makeOneGround(2)
            '''           '''
            '''           '''
            '''           '''
            '''           '''
            makeOneGround(7) 
            makeOneGround(8); makeOneWall(8)
            makeOneGround(9)
            makeOneGround(10)
            makeOneGround(11); makeOneThron(11, 2)
            '''           '''; makeOnePlatform(12.5)
            makeOneGround(14); makeOneThron(14, 3)
            makeOneGround(15)
            makeOnePlatform(16)
            makeOnePlatform(17)
            makeOnePlatform(18); makeOneFireball(18, 4)
            makeOnePlatform(19); makeOneFireball(19, 4)
            makeOnePlatform(20)
            makeOnePlatform(21); makeOneFireball(21, 3)
            makeOnePlatform(22)
            makeOnePlatform(23)
            makeOnePlatform(24)
            makeOnePlatform(25)
            makeOneGround(26); makelastPos(26)

        elif num == 2:

            makeOneGround(1)
            makeOneGround(2)
            makeOneGround(3) ; makeOneWall(3)
            makeOneGround(4) ; makeOneWall(4)
            makeOneGround(5) ; makeOneWall(5)
            makeOneGround(6)
            makeOneGround(7) ; makeOneThron(7, 1)
            makeOneGround(8)
            makeOneGround(9) ; makeOneWall(9)
            '''           '''; makeOneWall(10)
            '''           '''
            makeOneGround(12)
            makeOneGround(13); makelastPos(13)

        elif num == 3:

            makeOneGround(1)
            makeOneGround(2) ; makeOnePlatform(2) ; makeOneFireball(2, 2)
            makeOneGround(3) ; makeOnePlatform(3) ; makeOneFireball(3, 2)
            makeOneGround(4) ; makeOnePlatform(4) ; makeOneFireball(4, 2)
            makeOneGround(5) ; makeOnePlatform(5) ; makeOneFireball(5, 2)
            makeOneGround(6) ; makeOnePlatform(6)
            makeOneGround(7) ; makeOnePlatform(7) ; makeOneFireball(7, 1)
            makeOneGround(8) ; makeOnePlatform(8) ; makeOneFireball(8, 1)
            makeOneGround(9) ; makeOnePlatform(9) ; makeOneFireball(9, 1)
            makeOneGround(10); makeOneFireball(10, 1)
            makeOneGround(11)
            '''           '''
            '''           '''
            '''           '''; makeOnePlatform(14)
            '''           '''
            '''           '''
            makeOneGround(17)
            makeOneGround(18); makelastPos(18)

        elif num == 4:

            makeOneGround(1)
            '''           '''; 
            '''           '''
            '''           '''
            '''           '''
            makeOneGround(6)
            '''           '''
            '''           '''
            makeOneGround(9)
            '''           '''; makeOneWall(10)
            '''           '''
            '''           '''
            makeOneGround(13)
            '''           '''
            '''           '''
            '''           '''
            '''           '''
            makeOneGround(18)
            makeOneGround(19); makelastPos(19)

        elif num == 5:

            makeOneGround(1)
            '''           '''; makeOneFireball(2, 1)
            makeOneGround(3)
            '''           '''; makeOneFireball(4, 1)
            makeOneGround(5)
            makeOneGround(6)
            makeOneGround(7) ; makeOneFireball(7, 2); makeOneFireball(7, 3); makeOneFireball(7, 4); makeOneFireball(7, 5); makeOneFireball(7, 6); makeOneFireball(7, 7)
            makeOneGround(8)
            '''           '''
            '''           '''; makeOnePlatform(10)
            '''           '''; makeOnePlatform(11)
            '''           '''
            '''           '''
            '''           '''; makeOnePlatform(14)
            '''           '''
            '''           '''
            '''           '''
            '''           '''
            '''           '''
            '''           '''; makeOnePlatform(20)
            '''           '''
            '''           '''
            '''           '''
            makeOneGround(24); makeOneThron(24, 1)
            makeOneGround(25); makeOneThron(25, 1)
            makeOneGround(26)
            makeOneGround(27); makelastPos(27)

        elif num == 6:
            
            makeOneGround(1)
            '''           '''
            makeOneGround(3) ; makeOneThron(3, 2)
            '''           '''
            makeOneGround(5)
            makeOneGround(6) ; makeOneThron(6, 1)
            makeOneGround(7)
            makeOneGround(8) ; makeOneThron(8, 1)
            makeOneGround(9) ; makeOneThron(9, 1)
            makeOneGround(10)
            makeOneGround(11)
            makeOneGround(12); makeOneThron(12.5, 2)
            makeOneGround(13)
            makeOneGround(14)
            makeOneGround(15); makeOneFireball(15, 2)
            makeOneGround(16)
            makeOneGround(17); makelastPos(17)



        
    

    def move(self, speed):
        
        if self.state == 'platform':
            self.position -= np.array([speed, 1, speed, 1])
        else:
            self.position -= np.array([speed, 0, speed, 0])

    def collision_check(self, other):

        collision = self.overlap(self.position, other.position)

        # 땅이랑 닿아있다면
        if collision and other.position[3] <= self.position[1] + other.velocity + 4 and other.velocity >= 0:
            other.on_ground = True
            other.velocity = 0
            other.jump_count = 2

            # 조이스틱 하단바가 눌려있다면 (슬라이드 중 이라면)
            if not joystick.button_D.value:
                other.state = 'slide'
                other.position = np.array([30, self.position[1] - 30, 60, self.position[1]])
            else:
                other.state = 'run'
                other.position = np.array([30, self.position[1] - 60, 60, self.position[1]])

        # 캐릭터가 블럭 오른쪽으로 나갔을 때
        if (self.position[2] < other.position[0] and not self.is_out):
            other.on_ground = False
            self.is_out = True


    def overlap(self, rect1, rect2):
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[1] > rect2[3] or rect1[3] < rect2[1])