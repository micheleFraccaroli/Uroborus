import functions as f
import matplotlib.pyplot as plt

def plot_total_graph(file_path):
        (column_x,column_y) = f.file_import(file_path)
        # plotting array column
        trace1 = plt.plot(column_x, column_y)

        title = input("Inserisci il titolo del grafico: ")
        xname = input("Inserisci il nome dell'asse x: ")
        yname = input("Inserisci il nome dell'asse y: ")

        plt.suptitle(title, fontsize=12, fontweight='bold')
        plt.xlabel(xname, fontsize=20)
        plt.ylabel(yname, fontsize=20)
        plt.tick_params(labelsize=16)

        plt.show()