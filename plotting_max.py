import functions as f
import matplotlib.pyplot as plt

def plotting_max(column_x, column_y, interval):
    max_rel = [] # lista di massimi relativi da stampare a video
    I = [] #intervalli
    k = int(interval)

    for j in range(len(column_y)):
        if j < k:
            val = column_y[j]
            I.append(val)
        else:
            y=0
            for t in I:
                if y == 0:
                    var_1 = I[y]
                    if t > var_1 and t > I[y+1]:
                        max_rel.append(t)
                    y = y + 1
                elif y == len(I)-1:
                    var_1 = I[y]
                    if t > I[y-1] and t > var_1:
                        max_rel.append(t)
                    y = y + 1
                else:
                    if t > I[y-1] and t > I[y+1]:
                        max_rel.append(t)
                    y = y + 1
            k = j + int(interval)

    max_rel.sort()
    print('\nQuesti sono i massimi relativi che ho trovato nel file con intervalli di', interval,'dati\n', max_rel)
    My = []
    Mx = []
    # relative max works
    max_plot = input('\nInserisci il massimo che vuoi analizzare: ')
    if max_plot != 'q':
        amp_im = input("Inserisci l'intervallo d'ampiezza del plot dei massimi: ")
        if amp_im != 'q':
            for m in range(len(max_rel)):
                if max_rel.count(float(max_plot)) == 0:
                    print('\nElemento non trovato\n')
                    max_plot = input('Inserisci il massimo che vuoi analizzare: ')
                else:
                    index = column_y.index(float(max_plot))
                    for h in range((index-int(amp_im)),(index+int(amp_im))):
                        My.append(column_y[h])
                    for u in range((index-int(amp_im)),(index+int(amp_im))):
                        Mx.append((column_x[u]))
                break
            max_trace = plt.plot(Mx, My)

            title = input("Inserisci il titolo del grafico: ")
            xname = input("Inserisci il nome dell'asse x: ")
            yname = input("Inserisci il nome dell'asse y: ")

            plt.suptitle(title, fontsize=12, fontweight='bold')
            plt.xlabel(xname)
            plt.ylabel(yname)

            plt.show()
        else:
            op = f.switch()
    else:
        op = f.switch()