import pygame, sys
from util.CONTANTS import *
from cliente import client


class Pids:

    def __init__(self):
        self.tela = ""
        self.LIST_INIT = 0
        self.LIST_END = 22
        self.pid_list = self.update()

    def up(self):
        self.LIST_INIT += 20
        self.LIST_END += 20


    def down(self):
        self.LIST_INIT -= 20
        self.LIST_END -= 20

    #SET AN INTERVAL
    def set_interval(self):
        pass

    def update(self):
        return client.request_pid()

    def show_more(self):
        pos = pygame.mouse.get_pos()
        t = (200, 550)
        t2 = (550, 580)

        if t < pos > t2:  # esquerda
            if self.LIST_END > len(self.pid_list):
                pass
            else:
                self.up()
        elif t > pos < t2:  # direita
            if self.LIST_INIT == 0:
                pass
            else:
                self.down()
        self.montar_surface(self.tela)


    def montar_surface(self, tela):
        self.tela = tela
        pygame.display.set_caption("Lista de processos")


        process = pygame.surface.Surface((tela[1], tela[2]))
        process.fill(BRANCO)

        pygame.font.init()
        CALIBRI21 = pygame.font.SysFont('Calibri', 18)

        # this react only helps with position
        pygame.draw.rect(process, BTN_GREY, (18, 58, 762, 470), 1)
        pygame.draw.rect(process, BTN_GREY, (30, 550, int(tela[1] / 2 - 300), 30), 0)
        pygame.draw.rect(process, BTN_GREY, (int(tela[1] / 2 + 280), 550, 90, 30), 0)

        pid_text = CALIBRI21.render("voltar", 1, GREY)
        process.blit(pid_text, (60, 555))

        pid_text = CALIBRI21.render("próxima", 1, GREY)
        process.blit(pid_text, (tela[1] - 105, 555))

        counter = 20
        h_text = 50
        s_h = counter + h_text

        my_name = f"{'PID':<30}{'Nome':<53}{'Status':<20}{'Uso Cpu':<40}{'Threads'}"
        title_text = CALIBRI21.render(my_name, 1, PRETO)

        process.blit(title_text, (30, 30))

        for i in self.pid_list[self.LIST_INIT:self.LIST_END]:
            pis = str(i['pid']).encode(FORMAT)
            n = str(i['nam'][:30]).encode(FORMAT)
            s = str(i['st']).encode(FORMAT)
            m = str(i['mem'] + '%').encode(FORMAT)
            t = str(i['th']).encode(FORMAT)

            pid_text = CALIBRI21.render(pis, 1, PRETO)
            process.blit(pid_text, (30, s_h))

            name_text = CALIBRI21.render(n, 1, PRETO)
            process.blit(name_text, (120, s_h))

            status_text = CALIBRI21.render(s, 1, PRETO)
            process.blit(status_text, (400, s_h))

            mem_text = CALIBRI21.render(m, 1, PRETO)
            process.blit(mem_text, (500, s_h))

            threads_text = CALIBRI21.render(t, 1, PRETO)
            process.blit(threads_text, (700, s_h))

            s_h += 20

        tela[0].blit(process, (0, 0))

# def montar_tela():
#     width = 800
#     height = 600
#     tela = pygame.display.set_mode((width, height))
#     pygame.display.set_caption("System information")
#     tela.fill(BRANCO)
#     return [tela, width, height]
#
#
# def check_screen():
#     tela = montar_tela()
#     montar_surface(tela)
#
#
# def main():
#     global frags
#     pygame.init()
#     cont = 40
#     clock = pygame.time.Clock()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     frags = True
#                     print('space')
#                 if event.key == pygame.K_BACKSPACE:
#                     frags = False
#                     print('backspace')
#             elif event.type == MOUSEBUTTONDOWN:
#                 show_more()
#
#         if cont == 40:
#             check_screen()
#             cont = 0
#
#         pygame.display.update()
#         clock.tick(40)
#         cont = cont + 1
#
#
# if __name__ == '__main__':
#     main()
