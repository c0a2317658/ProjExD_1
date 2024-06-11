import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    
    kk_rct = kk_img.get_rect() #こうかトンレクとの中質
    kk_rct.center = 300,200

    speed = 1
    m_speed = 2 * speed
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img2, [-x+4800, 0])

        key_list = pg.key.get_pressed() #全キー
        m_x = -speed
        m_y = 0
        if key_list[pg.K_UP]: #上矢印が押されたら
            m_y -= speed
        if key_list[pg.K_DOWN]:
            m_y += speed
        if key_list[pg.K_RIGHT]:
            m_x += m_speed
        
        kk_rct.move_ip(m_x,m_y)
        screen.blit(kk_img, kk_rct.center)

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()