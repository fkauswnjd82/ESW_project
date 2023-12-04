from PIL import Image, ImageDraw
from Ground import Ground
from Character import Character
from Joystick import Joystick
import random

def main():
    
    # 이미지 경로로 가져오기
    stick_run_0_path = "/home/kau-esw/RunAndHit/image/Character_run_0.png"
    stick_run_1_path = "/home/kau-esw/RunAndHit/image/Character_run_1.png"
    stick_jump_path = "/home/kau-esw/RunAndHit/image/Character_jump.png"
    stick_slide_path = "/home/kau-esw/RunAndHit/image/Character_slide.png"
    background_path = "/home/kau-esw/RunAndHit/image/Background.png"
    wood_block_path = "/home/kau-esw/RunAndHit/image/WoodBlock.png"
    wood_wall_path = "/home/kau-esw/RunAndHit/image/WoodWall.png"
    thron_1_path = "/home/kau-esw/RunAndHit/image/Thron_1.png"
    thron_2_path = "/home/kau-esw/RunAndHit/image/Thron_2.png"
    thron_3_path = "/home/kau-esw/RunAndHit/image/Thron_3.png"
    fireball_0_path = "/home/kau-esw/RunAndHit/image/Fireball_0.png"
    fireball_1_path = "/home/kau-esw/RunAndHit/image/Fireball_1.png"
    platform_path = "/home/kau-esw/RunAndHit/image/Platform.png"
    start_path = "/home/kau-esw/RunAndHit/image/Start.png"
    gameover_path = "/home/kau-esw/RunAndHit/image/Gameover.png"
    
    stick_run_0_image = Image.open(stick_run_0_path)
    stick_run_1_image = Image.open(stick_run_1_path)
    stick_run_image = Image.open(stick_run_0_path)
    stick_jump_image = Image.open(stick_jump_path)
    stick_slide_image = Image.open(stick_slide_path)
    background_image = Image.open(background_path)
    wood_block_image = Image.open(wood_block_path)
    wood_wall_image = Image.open(wood_wall_path)
    thron_1_image = Image.open(thron_1_path)
    thron_2_image = Image.open(thron_2_path)
    thron_3_image = Image.open(thron_3_path)
    fireball_0_image = Image.open(fireball_0_path)
    fireball_1_image = Image.open(fireball_1_path)
    fireball_image = Image.open(fireball_0_path)
    platform_image = Image.open(platform_path)
    start_image = Image.open(start_path)
    gameover_image = Image.open(gameover_path)


    while True:

        # 기본 설정 초기화
        joystick = Joystick()
        my_image = Image.new("RGB", (joystick.width, joystick.height))
        my_draw = ImageDraw.Draw(my_image)
        joystick.disp.image(my_image)
        stickman = Character()

        # 시작 배경 흰색
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))

        # 애니메이션 효과 용 프레임 변수
        frame = 1

        # 씬 전환용 변수
        scene = 1

        # 여러 오브젝트 담을 변수
        grounds = []
        walls = []
        throns = []

         # 버튼이 한번만 눌렸는지 조사
        a_button_pressed = False
        d_button_pressed = False

        # 땅 생성
        Ground.makeMaps(grounds, walls, throns)

        # 시작 화면
        while scene == 1:
            if joystick.button_A.value and a_button_pressed:
                a_button_pressed = False

            if not joystick.button_A.value and not a_button_pressed:
                scene = 2
                a_button_pressed = True
            my_image.paste(start_image, (0, 0))
            joystick.disp.image(my_image)

        # 게임 화면
        while scene == 2:
            # 프레임은 1 ~ 120 반복
            if (frame == 120):
                frame = 1
            else:
                frame += 1

            # 프레임에 따른 캐릭터 달리기 및 파이어볼 모션 체인지
            if frame % 4 is (1 or 2):
                stick_run_image = stick_run_0_image
                fireball_image = fireball_0_image

            elif frame % 4 is (3 or 4):
                stick_run_image = stick_run_1_image
                fireball_image = fireball_1_image

        # 슬라이드 키 땠을 때
            if joystick.button_D.value and d_button_pressed:
                if stickman.state == 'slide':
                    stickman.replace()
                    if stickman.jump_count < 2:
                        stickman.state = 'jump'
                    else:
                        stickman.state = 'run'
                        d_button_pressed = False
            

            # 슬라이드 키 누르고 있을 때
            if not joystick.button_D.value:
                if stickman.on_ground:
                    stickman.state = 'slide'
                    d_button_pressed = True

            # 점프 키 땠을 때
            if joystick.button_A.value and a_button_pressed:
                a_button_pressed = False

            # 점프 키 눌렀을 때
            if not joystick.button_A.value and not a_button_pressed:
                stickman.jump()
                a_button_pressed = True
        
            # 캐릭터 중력 적용
            stickman.move()
            
        # 무한 루프 배경 그리기
            my_image.paste(background_image, (0 - frame * 2, 0))
            my_image.paste(background_image, (joystick.width - frame * 2, 0))

            # 스틱맨이 땅 위에 있는지를 False로 초기화
            stickman.on_ground = False

            # 땅, 플렛폼 드로잉 및 충돌체크 및 움직임 부분
            for ground in grounds:

                # 위치가 화면을 벗어나면 건너뛰고, 배열 개수가 너무 많아지면 삭제함
                if ground.position[0] < -30:
                    continue
                if len(grounds) > 100:
                    grounds = grounds[50:]
                # 그림 및 맵 추가 생성 조사
                if ground.state == 'ground':
                    my_image.paste(wood_block_image, (ground.position[0], ground.position[1]), wood_block_image)
                elif ground.state == 'platform':
                    my_image.paste(platform_image, (ground.position[0], ground.position[1]), platform_image)
                elif ground.state == 'lastPos':
                    # 만약 마지막 땅 x 위치가 210이라면 랜덤 맵 생성
                    if ground.position[0] == 210:
                        randInt = random.randint(1, 6)
                        Ground.makeMaps(grounds, walls, throns, randInt)
                        
                # 충돌영역
                #my_draw.rectangle(tuple(ground.position), outline = ground.outline, fill = None)
                
                # 장소영역은 충돌 안하게
                if ground.state != 'lastPos':
                    ground.collision_check(stickman)
                ground.move(stickman.speed)


            # 가시 드로잉 및 충돌체크 및 움직임 부분
            for thron in throns:
                
                # 위치가 화면을 벗어나면 건너뛰고, 배열 개수가 너무 많아지면 삭제함
                if thron.position[0] < -30:
                    continue
                if len(throns) > 100:
                    throns = throns[50:]
                # 그림
                if thron.state == 'one':
                    my_image.paste(thron_1_image, (thron.position[0] - 10, thron.position[1] - 10), thron_1_image)
                elif thron.state == 'two':
                    my_image.paste(thron_2_image, (thron.position[0] - 10, thron.position[1] - 10), thron_2_image)
                else:
                    my_image.paste(thron_3_image, (thron.position[0] - 10, thron.position[1] - 10), thron_3_image)
                # 충돌영역
                #my_draw.rectangle(tuple(thron.position), outline = thron.outline, fill = None)
                thron.collision_check(stickman)
                thron.move(stickman.speed)


            # 벽, 파이어볼 드로잉 및 충돌체크 및 움직임 부분
            for wall in walls:
                
                # 위치가 화면을 벗어나면 건너뛰고, 배열 개수가 너무 많아지면 삭제함
                if wall.position[0] < -30:
                    continue
                if len(walls) > 100:
                    walls = walls[50:]
                
                # 그림
                if wall.state == 'wall':
                    my_image.paste(wood_wall_image, (wall.position[0] - 10, wall.position[1]), wood_wall_image)
                elif wall.state == 'fireball':
                    my_image.paste(fireball_image, (wall.position[0] - 10, wall.position[1] - 10), fireball_image)
                # 충돌영역
                #my_draw.rectangle(tuple(wall.position), outline = '#FF0000', fill = None)
                wall.collision_check(stickman)
                wall.move(stickman.speed)
        
            # 스틱맨 그림
            if stickman.state == 'run':
                my_image.paste(stick_run_image, (stickman.position[0], stickman.position[1]), stick_run_image)
            elif stickman.state == 'slide':
                my_image.paste(stick_slide_image, (stickman.position[0] - 30, stickman.position[1]), stick_slide_image)
            else:
                my_image.paste(stick_jump_image, (stickman.position[0], stickman.position[1]), stick_jump_image)

            # 스틱맨 충돌영역
            #my_draw.rectangle(tuple(stickman.position), outline = stickman.outline, fill = None)

            # 죽었는지 조사
            if stickman.state == 'die' or stickman.position[1] > 240:
                for i in range(0, 241, 10):
                    my_draw.rectangle((240 - i, 0, 240, 240), outline = '#000000', fill = '#000000')
                    joystick.disp.image(my_image)
                scene = 3

            # 화면 띄우기
            if frame % 2 == 0:
                joystick.disp.image(my_image)
        
        # 게임 오버 화면
        while scene == 3:
            if not joystick.button_A.value:
                scene = 1
            my_image.paste(gameover_image, (0, 0))
            joystick.disp.image(my_image)

        

if __name__ == '__main__':
    main()