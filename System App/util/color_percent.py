def def_percent_color(percent):
    percent = int(percent)
    global cores
    r = 0
    g = 255
    b = 255

    for n in range(0, int(round(percent))):
        r += 2
        g -= 2
        b -= 2
        cores = (r, g, b)
    return cores