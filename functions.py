import fileinput
import csv

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
    finally:
        f.close()
        r.close()

    return column_x_1, column_y_1

def switch():
    op = input("\n\n --------------------- Make choice ---------------------\n\n1) Plotting total graph\n2) Max of graph\n3) Subtraction between graphs\n4) Multi-plotting graph\n\nMake your choice ('q' for term the app): ")
    return op
# -------------------------------------------