import pygame
from util.CONTANTS import BRANCO, BACKGROUND_COLOR, GREY, PRETO, BTN_GREY
from util.color_percent import def_percent_color
from cliente.client import request_space


class Disk:
    def __init__(self):
        self.tela = ""
        self.parts = self.update_parts()

    def update_parts(self):
        return request_space()

    def montar_surface(self, tela):
        self. tela = tela
        pygame.display.set_caption("Discos do Computador")

        parts = self.update_parts()

        pygame.font.init()
        CALIBRI21 = pygame.font.SysFont('Calibri', 21)
        CALIBRI27 = pygame.font.SysFont('Calibri', 27)

        graph = pygame.surface.Surface((tela[1] - 150, 400))
        graph.fill(BRANCO)
        info = pygame.surface.Surface((800, 200))
        info.fill(BRANCO)

        title_text = CALIBRI27.render("DISCOS DO COMPUTADOR", 1, PRETO)
        info.blit(title_text, (10, 10))

        pygame.draw.line(info, BACKGROUND_COLOR, (0, info.get_height()-20), (800-15, info.get_height()-20), 7)

        title_text = CALIBRI21.render("100", 1, GREY)
        tela[0].blit(title_text, (45, 800/3.5))
        title_text = CALIBRI21.render("50", 1, GREY)
        tela[0].blit(title_text, (45, tela[0].get_height()/2+100))
        title_text = CALIBRI21.render("0", 1, GREY)
        tela[0].blit(title_text, (45, tela[0].get_height()-30))

        #  counters
        c = 70
        ct = 0
        y = 3
        x = 2
        desl = 20
        alt = graph.get_height() - 1 * 10
        larg = (graph.get_width() - 5 * y - (1 + ct) * desl) / 2
        d = x + desl

        for i in parts:  # loop for each disk partition
            disk_name = str(list(i.keys())[0])
            disk_percent = str(list(i.values())[0][3])
            disk_size = str(round(list(i.values())[0][0] / (1024 * 1024 * 1000)))
            title_text = CALIBRI21.render(f"{disk_name} {disk_percent}% em uso de {disk_size}GB", 1, PRETO)
            info.blit(title_text, (30, c))

            #  draws rectangles for disks graph
            pygame.draw.rect(graph, def_percent_color(int(float(disk_percent))+10), (d, y, larg, alt))
            pygame.draw.rect(graph, BRANCO, (d, y, larg, (1 - int(float(disk_percent)) / 120) * alt))

            #  adds to counters
            d = d + larg + desl
            ct += 1
            c += 30

        #  draws lines to cut across disks rectangles
        pygame.draw.rect(graph, BRANCO, (10, 40, 30, graph.get_height()))
        pygame.draw.line(graph, BTN_GREY, (10, 65), (800, 65), 1)
        pygame.draw.line(graph, BTN_GREY, (10, graph.get_height()/2+30), (800, graph.get_height()/2+30), 1)
        pygame.draw.line(graph, BTN_GREY, (10, graph.get_height()-7), (800, graph.get_height()-7), 1)

        #  binds everything to corresponding surfaces
        tela[0].blit(graph, (90, tela[2] - 400))
        tela[0].blit(info, (10, 10))
