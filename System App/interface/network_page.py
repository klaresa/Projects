import pygame
from util.CONTANTS import BRANCO, PRETO, GREY
from cliente.client import request_net, request_gateway, request_ip


class Network:

    def __init__(self):
        self.tela = ""
        self.net = request_net()
        self.gateway = request_gateway()
        self.ip = request_ip()

    def update_net(self):
        net = request_net()
        self.net = net

    def update_gateway(self):
        gateway = request_gateway()
        self.gateway = gateway

    def mostrar_surface(self, tela):
        self. tela = tela
        pygame.display.set_caption("Network")

        ip = list(self.ip)[0]
        parts = self.net
        gateway = self.gateway

        pygame.font.init()
        CALIBRI18 = pygame.font.SysFont('Calibri', 18)
        CALIBRI25 = pygame.font.SysFont('Calibri', 25)

        info = pygame.surface.Surface((800, 600))
        info.fill(BRANCO)
        # pygame.draw.rect(info, BTN_GREY, (18, 58, 762, 470), 1)

        title_text = CALIBRI25.render(f"GATEWAY: {gateway}", 1, PRETO)
        info.blit(title_text, (info.get_width()-300, 10))
        title_text = CALIBRI25.render(f"IP: {ip}", 1, PRETO)
        info.blit(title_text, (info.get_width()-300, 40))

        c = 100
        for i in parts:
            net_name = str(list(i.keys())[0])
            net_name_ip = str(list(i.values())[0])
            submask_value = str(list(i.values())[1])
            mac_value = str(list(i.values())[2])

            title_text = CALIBRI25.render(f"{net_name}", 1, PRETO)
            info.blit(title_text, (30, c))

            title_text = CALIBRI18.render(f"IP: {net_name_ip}           Submask: {submask_value}            MAC: {mac_value}", 1, GREY)
            info.blit(title_text, (30, c+40))
            c += 100

        tela[0].blit(info, (0, 0))
