import matplotlib.pyplot as plt
def draw_line():
    lines = []
    ax = plt.gca()
    xy = plt.ginput(2)
    x = [p[0] for p in xy]
    y = [p[1] for p in xy]
    line = plt.plot(x,y)
    ax.figure.canvas.draw()
    lines.append(line)
    return x,y
