import pygame
import os
import time
import sys
pygame.font.init()

Credit_Font = pygame.font.SysFont("comiscans", 23)

Display_Width = 800
Display_Height = 800
Block_Width = Display_Width // 8
Block_Height = Display_Height // 8

chess_board = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "cb.png")))
emilia = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "emilia-tan2.jpg")))
lb_tile = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "lightbrown.jpg")))
db_tile = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "darkbrown.jpg")))


chess_board = pygame.transform.scale(chess_board, (Display_Width, Display_Height))
emilia = pygame.transform.scale(emilia, (Block_Width, Block_Height))
lb_tile = pygame.transform.scale(lb_tile, (Block_Width, Block_Height))
db_tile = pygame.transform.scale(db_tile, (Block_Width, Block_Height))

win = pygame.display.set_mode((Display_Width, Display_Height))

def main():
    print(type(emilia))
    is_running = True
    counter = 0

    pre_click_pos = (-1, -1)

    b = Board(0, 0, is_running)
    s = Square(0, 0)

    b.draw()

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.MOUSEBUTTONUP:
                # pos = (x, y), pos[0] = x, pos[1] = y
                pos = pygame.mouse.get_pos()
                print(f'Previous: {pre_click_pos}, Current: {pos}')
                if pre_click_pos == s.sqare_clicked(pos):
                    s.remove(pre_click_pos)
                else:
                    s.draw(s.sqare_clicked(pos))
                    if counter > 0:
                        s.remove(pre_click_pos)

                counter += 1
                pre_click_pos = s.sqare_clicked(pos)


class Board:
    def __init__(self, x, y, running):
        self.x = x
        self.y = y
        self.running = running

    def draw(self):
        win.blit(chess_board, (self.x, self.y))
        pygame.display.update()

class Square:
    def __init__(self, x, y):
        self.Row = x
        self.Col = y

    def sqare_clicked(self, mouse_pos):
        sqr_clicked = []
        for i in range(0, Display_Width, Block_Width):
            if i <= mouse_pos[0] < i + Block_Width:
                sqr_clicked.append(i)
        for j in range(0, Display_Height, Block_Height):
            if j <= mouse_pos[1] < j + Block_Height:
                sqr_clicked.append(j)

        return sqr_clicked

    def draw(self, pos):
        win.blit(emilia, (pos[0], pos[1]))
        pygame.display.update()

    def remove(self, pos):
        x_val = pos[0] / 100
        y_val = pos[1] / 100

        if x_val % 2 == 0 and y_val % 2 == 0:
            win.blit(lb_tile, (pos[0], pos[1]))
        elif x_val % 2 == 0 and y_val % 2 != 0:
            win.blit(db_tile, (pos[0], pos[1]))
        elif x_val % 2 != 0 and y_val % 2 == 0:
            win.blit(db_tile, (pos[0], pos[1]))
        else:
            win.blit(lb_tile, (pos[0], pos[1]))

        pygame.display.update()

main()