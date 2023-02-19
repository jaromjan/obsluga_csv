# Program do obslugi plikow csv
import sys
import csv
import os

if len(sys.argv) < 1:
    print('Nie podano zadnych argumentow')
elif len(sys.argv) < 3:
    print('Nie podano danych do zmiany')
else:
    plik_in = sys.argv[1]
    plik_out = sys.argv[2]
    dlugosc = len(sys.argv)
    if not os.path.exists(plik_in):
        print('Plik zrodlowy nie istnieje !!')
        quit()
    print(f'Podano: plik wejsciowy: {plik_in} , plik docelowy: {plik_out}\n'
          f'zakres zmian: {sys.argv[3:]}\n'
          f'Odczytuje plik wejsciowy i wyswietlam jego zawartosc:')
    with open(plik_in, 'r') as f:
        reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC, delimiter = ',')
        dane  = []
        # obliczam liczbe rekordow i dlugosc rekordu
        lw = 0
        dw = 0
        for line in reader:
            dane.append(line)
            print(line)
            lw += 1
            if dw < len(line):
                dw = len(line)
    if len(sys.argv) < 4:
        print('Nie podano danych do zmiany')
        quit()
    kont = 0
    m = 3
    while m < dlugosc:
        zm = sys.argv[m].split(",")
        if lw < int(zm[0]) or dw < int(zm[1]) or len(zm) != 3:
            print(f'zmiana: {sys.argv[m]} zawiera bledna wartosc')
            kont = 1
        m += 1
    if kont == 0:
        i = 3
        print('Wprowadzam zmiany')
        while i < dlugosc:
            wsad = sys.argv[i].split(",")
            x = int(wsad[0])
            y = int(wsad[1])
            dane[x][y] = wsad[2]
            i += 1
        print(f'Zapisuje plik: {plik_out} i wyswietlam jego zawartosc:')
        with open(plik_out, 'w' , newline='') as f:
            writer = csv.writer(f, quoting = csv.QUOTE_NONNUMERIC, delimiter = ',')
            tabela = dane
            for line in tabela:
                writer.writerow(line)
                print(line)
