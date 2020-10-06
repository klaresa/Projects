import pygame
from util.color_percent import def_percent_color
from util.CONTANTS import BRANCO, PRETO
from cliente.client import request_stat, request_cpu


class Cpus:

    def __init__(self):
        self.tela = ""
        self.stats = request_stat()
        self.cpus = self.update_cpu()
        self.stats = self.update_stats()

    def update_stats(self):
        return request_stat()

    def update_cpu(self):
        return request_cpu()

    def mostra_texto(self, s1, nome, chave, pos_y):
        pygame.font.init()
        CALIBRI21 = pygame.font.SysFont('Calibri', 21)
        text = CALIBRI21.render(nome, True, PRETO)
        s1.blit(text, (10, pos_y))
        if chave == "freq":
            s = str(round(self.stats['freq'], 2))
        elif chave == "nucleos":
            s = str(self.stats['cpu_count'])
            s = s + " (" + str(self.stats['cpu_lol']) + ")"
        else:
            s = str(self.stats['cpu_info'][chave])
        text = CALIBRI21.render(s, True, PRETO)
        s1.blit(text, (190, pos_y))

    def mount_cpu_page(self, tela):
        cpus = self.update_cpu()

        surf = pygame.surface.Surface((800, 200))
        surf.fill(BRANCO)
        self.mostra_texto(surf, "Nome: ", "brand_raw", 10)
        self.mostra_texto(surf, "Arquitetura: ", "arch", 30)
        self.mostra_texto(surf, "Palavra (bits): ", "bits", 50)
        self.mostra_texto(surf, "Frequência (MHz): ", "freq", 70)
        self.mostra_texto(surf, "Núcleos (físicos): ", "nucleos", 90)

        surface = pygame.surface.Surface((800, 480))
        surface.fill(BRANCO)
        num_cpu = len(cpus) - 1
        x = y = 10
        desl = 100
        alt = surface.get_height() - 2 * y
        larg = (surface.get_width() - 2 * y - (num_cpu + 1) * desl) / num_cpu
        d = x + desl
        for i in cpus[1:]:
            per_number = int(list(i.values())[0])
            pygame.draw.rect(surface, def_percent_color(per_number), (d, y, larg, alt))
            pygame.draw.rect(surface, PRETO, (d, y, larg, (1 - int(per_number) / 100) * alt))
            d = d + larg + desl

        tela[0].blit(surf, (0, 0))
        tela[0].blit(surface, (0, 600 / 5))
        pygame.display.flip()
