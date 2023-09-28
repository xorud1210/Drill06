import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running, pos_hand

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            pos_hand.append((event.x, TUK_HEIGHT - 1 - event.y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move_character():
    global frame, pos_cha, pos_hand, left
    x1, y1 = pos_hand[0]
    x2, y2 = pos_hand[1]
    pos_hand.remove(pos_hand[0])
    for i in range(0, 100, 1):
        handle_events()
        t = i / 100

        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        for x_h, y_h in pos_hand:
            hand.draw(x_h, y_h)
        if (x1 < x2):  # 오른쪽으로 갈때
            left = False
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:          # 왼쪽으로 갈때
            left = True
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)
    pos_cha = pos_hand[0]


running = True
left = True
pos_cha = (TUK_WIDTH // 2, TUK_HEIGHT // 2)
pos_hand = [(TUK_WIDTH // 2, TUK_HEIGHT // 2)]
frame = 0

while running:
    handle_events()
    if(len(pos_hand) > 1):
        move_character()
    else:       # 마우스 입력이 없을때 -> idle
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if left:        # 왼쪽 idle 애니메이션
            character.clip_draw(frame * 100, 100 * 2, 100, 100, pos_cha[0], pos_cha[1])
        else:           # 오른쪽 idle 애니메이션
            character.clip_draw(frame * 100, 100 * 3, 100, 100, pos_cha[0], pos_cha[1])
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
close_canvas()