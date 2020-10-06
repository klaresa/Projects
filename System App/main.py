import pygame, sys
from pygame.locals import *
from util.CONTANTS import *
from util.color_percent import def_percent_color
from interface.cpus_page import Cpus
from interface.screen_files import Pids
from interface.memory_page import Memory
from interface.disk_page import Disk
from interface.network_page import Network
from interface.home_page import Home

frags = False

pids = Pids()
cpus = Cpus()
memory = Memory()
disk = Disk()
network = Network()
home = Home()

pages = {
    "cpu_pag": True,
    "mem_pag": False,
    "disk_pag": False,
    "ip_pag": False,
    "pid_page": False
}


def resetar():
    global pages
    pages = {
        "cpu_pag": True,
        "mem_pag": False,
        "disk_pag": False,
        "ip_pag": False,
        "pid_page": False
    }

def carro():
    res = None
    temp = iter(pages)
    for key in temp:
        if pages[key]:
            pages[key] = False
            res = next(temp, None)
            pages[res] = True
            #  print(key, res, lista[res])
            if res == None:
                resetar()

def montar_surface(tela, lista, title, num):
    global msg_text

    pygame.font.init()
    CALIBRI21 = pygame.font.SysFont('Calibri', 21)
    CALIBRI27 = pygame.font.SysFont('Calibri', 27)

    larg = tela[1] - 2 * 20

    surface = pygame.surface.Surface((tela[1], tela[2]))
    surface.fill(BRANCO)

    if len(lista) == 1:
        usage = title[0] + str(lista[0])

    if len(lista) > 1:
        usage = title[0] + str(lista[0]) + "%"

        cor = def_percent_color(lista[0])
        pygame.draw.rect(surface, PRETO, (20, 50, larg, 30), 2)

        per = larg * lista[0] / 100
        pygame.draw.rect(surface, cor, (26, 56, int(per), 19), 0)

        counter = 20
        for i in lista[1:]:
            cpu_percent_text = "- " + title[lista.index(i)] + str(i)
            msg_text = CALIBRI21.render(cpu_percent_text, 1, PRETO)
            surface.blit(msg_text, (counter, 90))
            counter += 200

    title_text = CALIBRI27.render(usage, 1, PRETO)
    surface.blit(title_text, (10, 10))

    tela[0].blit(surface, (0, num))

# HOME SCREEN
def show_surfaces(tela):
    home.montar_surface(tela)

# frags or whole screen?
def check_screen():
    tela = montar_tela()
    if not frags:  # IF home screen
        show_surfaces(tela)  # passar para o home e mostrar surfaces

    if frags:  # IF out of home screen
        show_fragments(tela)  # passar para frags

# carrosel pages
def show_fragments(tela):
    # tela de CPUS
    if pages['cpu_pag']:
        cpus.mount_cpu_page(tela)

    # tela de MEMÓRIA
    elif pages['mem_pag']:
        memory.montar_surface(tela)

    # tela de DISCO
    elif pages['disk_pag']:
        disk.montar_surface(tela)

    # tela de INTERNET
    elif pages['ip_pag']:
        network.mostrar_surface(tela)

    # tela de PROCESSOS
    elif pages['pid_page']:
        pids.montar_surface(tela)

    pygame.display.flip()

def montar_tela():
    width = 800
    height = 600
    tela = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Informações Principais")
    tela.fill(BRANCO)
    return [tela, width, height]

def main():
    global frags
    pygame.init()
    cont = 40
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    frags = True
                    carro()
                if event.key == pygame.K_BACKSPACE:
                    frags = False
            elif event.type == MOUSEBUTTONDOWN:
                if pages['pid_page']:
                    pids.show_more()

        if cont == 40:
            check_screen()
            cont = 0

        pygame.display.update()
        clock.tick(40)
        cont = cont + 1

if __name__ == '__main__':
    main()
