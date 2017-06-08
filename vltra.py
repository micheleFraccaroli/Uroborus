#-----------------------------------------------------------------------------
#                                    Vltra
#
#                           Designed and developed by:
#                               Michele Fraccaroli
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-----------------------------------------------------------------------------


# import sys
# import string
import fileinput
import csv
import matplotlib.pyplot as plt
import numpy as np


# function-----------------------------------
def point_calc(number_string):
    num = number_string.split('E')
    base = float(num[0])
    exp = float(num[1])
    ris = (base) * 10 ** (exp)
    return ris

def column_creation(row, column_x, column_y, res):
    da_1 = point_calc((row[0]))
    column_x.append((da_1))
    da_2 = point_calc((row[1].strip('\n')))
    column_y.append((da_2))
    res.writerow((da_1, da_2))

def file_import(file):
    f = open(file, "r")
    u = 0
    while u < 2:
        fread_f = f.readline()
        if fread_f[0].isalpha():
            u = u + 1
        else:
            f.seek(0)
            u = u + 1
    fread_f_tot = f.read()
    fread_l = fread_f_tot.count(('\n'))

    f1 = open("file.dat/dati.dat", "w")
    f1.write(fread_f_tot)
    f1.close()
    w = open("file.dat/dati.dat", "r")
    r = open("file.dat/dati.csv", "w")
    # creation file .csv put in 2 columns and generated a data structure
    column_x = []
    column_y = []
    try:
        res = csv.writer(r)
        res.writerow(('D1', 'D2'))
        for i in range(fread_l):
            w1 = w.readline()
            try:
                row = w1.split(" ")
                column_creation(row, column_x, column_y, res)
            except ValueError:
                row = w1.split("\t")
                column_creation(row, column_x, column_y, res)
    finally:
        f.close()
        r.close()

    return column_x, column_y

def file_import_sub(file, i):
    f = open(file, "r")
    u = 0
    while u < 2:
        fread_f = f.readline()
        if fread_f[0].isalpha():
            u = u + 1
        else:
            f.seek(0)
            u = u + 1
    fread_f_tot = f.read()
    fread_l = fread_f_tot.count(('\n'))
    if i == '1':
        f1 = open("file.dat/dati_A.dat", "w")
        f1.write(fread_f_tot)
        f1.close()
        w = open("file.dat/dati_A.dat", "r")
        r = open("file.dat/dati_A.csv", "w")
    else:
        f1 = open("file.dat/dati_A2.dat", "w")
        f1.write(fread_f_tot)
        f1.close()
        w = open("file.dat/dati_A2.dat", "r")
        r = open("file.dat/dati_A2.csv", "w")
    # creation file .csv put in 2 columns and generated a data structure
    column_x_1 = []
    column_y_1 = []
    try:
        res = csv.writer(r)
        res.writerow(('D1', 'D2'))
        for i in range(int(fread_l/2)):
            w1 = w.readline()
            try:
                row = w1.split("\t")
                column_creation(row, column_x_1, column_y_1, res)
            except ValueError:
                row = w1.split(" ")
                column_creation(row, column_x_1, column_y_1, res)
            '''
            row = w1.split("\t")
            da_1a = point_calc((row[0]))
            column_x_1.append((da_1a))
            da_2a = point_calc((row[1].strip('\n')))
            column_y_1.append((da_2a))
            res.writerow((da_1a, da_2a))
            '''
    finally:
        f.close()
        r.close()

    return column_x_1, column_y_1

def switch():
    op = input("\n\n --------------------- Make choice ---------------------\n\n1) Plotting total graph\n2) Max of graph\n3) Subtraction between graphs\n4) Multi-plotting graph\n\nMake your choice ('q' for term the app): ")
    return op
# -------------------------------------------


print("\n --------------------- WELCOME TO VLTRA ---------------------\n")
op = switch()
column_x = []
column_y = []
file = []

while 1:
    if op == 'q' or op == 'Q':
        print("\nVltra termined!\n")
        break
# Plotting total graph -----------------------------------------------
    elif op == '1':
        file = input("Inserisci file .pss: ")
        file_path = ("Input_file/s1_2/" + file)
        try:
            if file != 'q':
                (column_x,column_y) = file_import(file_path)
                # plotting array column
                trace1 = plt.plot(column_x, column_y)
                #trace2 = plt.plot(column_x)
                #trace3 = plt.plot(column_y)
                title = input("Inserisci il titolo del grafico: ")
                xname = input("Inserisci il nome dell'asse x: ")
                yname = input("Inserisci il nome dell'asse y: ")

                plt.suptitle(title, fontsize=12, fontweight='bold')
                plt.xlabel(xname)
                plt.ylabel(yname)
                plt.show()
            else:
                op = switch()
        except IOError:
            print("Oops! An error has occurred, try again!\n")
# Plotting max------------------------------------------------
    elif op == '2':
        # research and plot max of the data ------------------------------------------------------------------------------------
        try:
            if not file:
                file = input("Inserisci file .pss: ")
                file_path = ("Input_file/s1_2/" + file)
                (column_x,column_y) = file_import(file_path)

            if file != 'q':
                interval = input("Inserisci il numero di elemnti in un intervallo per migliorare la precisione dei massimi: ")
                if interval != 'q':
                    max_rel = [] # lista di massimi relativi da stampare a video
                    I = [] # intervalli
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
                            file = input("Inserisci il nome del file con estensione .pss o premi 'q' per terminare: ")  
                        else:
                            op = switch()
                    else:
                        op = switch()
                else:
                    op = switch()
            else: 
                op = switch()
        except (IOError, ValueError):
            print("Oops! An error has occurred!\n")
        
# Plotting subtraction-----------------------------------------------------------------------------------------------------
    elif op == '3':
        column_x_1 = []
        column_y_1 = []
        column_x_2 = []
        column_y_2 = []
        column_ris = []
        trace_ris = []

        data1 = input('Inserisci il primo file: ')
        data2 = input('Inserisci il secondo file: ')
        data1_path = ("Input_file/s3/" + data1)
        data2_path = ("Input_file/s3/" + data2)
        legend = input("Inserisci legenda: ")
        try:
            if data1 != 'q' or data2 != 'q':
                while(data1 != 'ok' or data2 != 'ok'):
                    (column_x_1, column_y_1) = file_import_sub(data1_path, 1)
                    (column_x_2, column_y_2) = file_import_sub(data2_path, 2)

                    for i in range(len(column_y_1)):
                        column_ris.append(float(column_y_1[i]) - float(column_y_2[i]))

                    trace_ris.append(plt.plot(column_x_1, column_ris, label=legend))
                    column_ris.clear()
                    data1 = input("Inserisci il primo file('ok' per eseguire): ")
                    data2 = input("Inserisci il secondo file('ok' per eseguire): ")
                    data1_path = ("Input_file/s3/" + data1)
                    data2_path = ("Input_file/s3/" + data2)
                    if data1 == 'ok' or data2 == 'ok':
                        break
                    else:
                        legend = input("Inserisci legenda: ")

                let = plt.legend()
                let.draggable()
                title = input("Inserisci il titolo del grafico: ")
                xname = input("Inserisci il nome dell'asse x: ")
                yname = input("Inserisci il nome dell'asse y: ")

                plt.suptitle(title, fontsize=12, fontweight='bold')
                plt.xlabel(xname)
                plt.ylabel(yname)

                plt.show()
            else:
                op = switch()
        except IOError:
            print("Oops! An error has occurred, try again!\n")
# Multi-plotting-----------------------------------------------------------------------------------------------
    elif op == '4':
        column_x = []
        column_y = []
        trace = []
        i = 0

        files = input("Inserisci file ('ok' per eseguire, 'q' per terminare): ")
        files_path = ("Input_file/s4/" + files)
        legend = input("Inserisci legenda: ")

        if files == 'q' or files == 'Q':
            op = switch()
        else:
            try:
                while (files != 'ok'):
                    (column_x, column_y) = file_import(files_path)
                    trace.append(plt.plot(column_x, column_y, label=legend))
                    i = i + 1
                    files = input("Inserisci file ('ok' per eseguire, 'q' per terminare): ")
                    files_path = ("Input_file/s4/" + files)
                    if files != 'ok':
                        legend = input("Inserisci legenda: ")

                title = input("Inserisci il titolo del grafico: ")
                xname = input("Inserisci il nome dell'asse x: ")
                yname = input("Inserisci il nome dell'asse y: ")

                let = plt.legend()
                let.draggable()
                plt.suptitle(title, fontsize=12, fontweight='bold')
                plt.xlabel(xname)
                plt.ylabel(yname)
                
                plt.show()
            except IOError:
                print("Oops! An error has occurred, try again!\n")
# ------------------------------------------------------------------------------------------------------------
    else:
        print("\nChoice not avaible. Retry!\n")
        op = switch()
