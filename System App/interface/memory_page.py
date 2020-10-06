import pygame
from util.CONTANTS import BRANCO, BACKGROUND_COLOR, GREY, PRETO, BTN_GREY
from cliente.client import request_mem
from util.color_percent import def_percent_color


class Memory:
    def __init__(self):
        self.tela = ""
        self.memory = self.update_mem()
        self.uso_mem = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def update_mem(self):
        return request_mem()

    def update(self):
        self.uso_mem.pop(0)
        self.uso_mem.append(int(float(self.update_mem()['percent'])))

    def montar_surface(self, tela):
        self. tela = tela
        pygame.display.set_caption("Memória do Computador")

        pygame.font.init()
        CALIBRI21 = pygame.font.SysFont('Calibri', 21)
        CALIBRI27 = pygame.font.SysFont('Calibri', 27)
        CALIBRI40 = pygame.font.SysFont('Calibri', 77)

        graph = pygame.surface.Surface((tela[1] - 150, 400))
        graph.fill(BRANCO)
        info = pygame.surface.Surface((800, 200))
        info.fill(BRANCO)

        self.update()

        title_text = CALIBRI27.render("MEMÓRIA DO COMPUTADOR", 1, PRETO)
        info.blit(title_text, (10, 10))
        title_text = CALIBRI21.render(str(self.memory['total'])[:6]+"MB total", 1, PRETO)
        info.blit(title_text, (30, 70))
        title_text = CALIBRI21.render(str(self.memory['available'])[:6]+"MB disponíveis", 1, PRETO)
        info.blit(title_text, (30, 100))

        title_text = CALIBRI40.render(str(self.uso_mem[-1])+"%", 1, def_percent_color(self.uso_mem[-1]))
        info.blit(title_text, (info.get_width()-170, 50))
        title_text = CALIBRI21.render("em uso", 1, PRETO)
        info.blit(title_text, (info.get_width()-100, 120))

        pygame.draw.line(info, BACKGROUND_COLOR, (0, info.get_height()-20), (800-15, info.get_height()-20), 7)

        pygame.draw.rect(graph, BRANCO, (10, 40, 30, graph.get_height()))
        pygame.draw.line(graph, BTN_GREY, (10, 65), (800, 65), 1)
        pygame.draw.line(graph, BTN_GREY, (10, graph.get_height()/2+30), (800, graph.get_height()/2+30), 1)
        pygame.draw.line(graph, BTN_GREY, (10, graph.get_height()-7), (800, graph.get_height()-7), 1)

        title_text = CALIBRI21.render("100", 1, GREY)
        tela[0].blit(title_text, (45, 800/3.5))
        title_text = CALIBRI21.render("50", 1, GREY)
        tela[0].blit(title_text, (45, tela[0].get_height()/2+100))
        title_text = CALIBRI21.render("0", 1, GREY)
        tela[0].blit(title_text, (45, tela[0].get_height()-30))


        num_cpu = len(self.uso_mem) - 1
        y = 3
        x = 2
        desl = 10
        alt = graph.get_height() - 1 * 10
        larg = (graph.get_width() - 5 * y - (num_cpu + 1) * desl) / num_cpu
        d = x + desl

        for i in self.uso_mem:
            pygame.draw.rect(graph, PRETO, (d, y, larg, alt))
            pygame.draw.rect(graph, BRANCO, (d, y, larg, (1 - i / 120) * alt))
            d = d + larg + desl

        tela[0].blit(graph, (90, tela[2] - 400))
        tela[0].blit(info, (10, 10))

