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
    pass


running = True
pos_hand = [(TUK_WIDTH / 2, TUK_HEIGHT / 2)]

while running:
    handle_events()
    move_character()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for x, y in pos_hand:
        hand.draw(x,y)
    update_canvas()
close_canvas()