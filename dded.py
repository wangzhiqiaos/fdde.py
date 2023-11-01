import os
import sys
import cfg
import pygame
from modules import *
 
 
'''游戏主程序'''
def main():
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('开心消消乐🎃')
    # 加载背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(cfg.ROOTDIR, "resources/audios/bg.mp3"))
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
    # 加载音效
    sounds = {}
    sounds['mismatch'] = pygame.mixer.Sound(os.path.join(cfg.ROOTDIR, 'resources/audios/badswap.wav'))
    sounds['match'] = []
    for i in range(6):
        sounds['match'].append(pygame.mixer.Sound(os.path.join(cfg.ROOTDIR, 'resources/audios/match%s.wav' % i)))
    # 加载字体
    font = pygame.font.Font(os.path.join(cfg.ROOTDIR, 'resources/font/font.TTF'), 25)
    # 图片加载
    gem_imgs = []
    for i in range(1, 8):
        gem_imgs.append(os.path.join(cfg.ROOTDIR, 'resources/images/gem%s.png' % i))
    # 主循环
    game = gemGame(screen, sounds, font, gem_imgs, cfg)
    while True:
        score = game.start()
        flag = False
        # 一轮游戏结束后玩家选择重玩或者退出
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP and event.key == pygame.K_r:
                    flag = True
            if flag:
                break
            screen.fill((135, 206, 235))
            text0 = 'Final score: %s' % score
            text1 = 'Press <R> to restart the game.'
            text2 = 'Press <Esc> to quit the game.'
            y = 150
            for idx, text in enumerate([text0, text1, text2]):
                text_render = font.render(text, 1, (85, 65, 0))
                rect = text_render.get_rect()
                if idx == 0:
                    rect.left, rect.top = (212, y)
                elif idx == 1:
                    rect.left, rect.top = (122.5, y)
                else:
                    rect.left, rect.top = (126.5, y)
                y += 100
                screen.blit(text_render, rect)
            pygame.display.update()
        game.reset()
 
 
'''run'''
if __name__ == '__main__':
    main()
