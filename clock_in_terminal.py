#!/usr/bin/env python3

import time
import os

a1 = [[' ', ' ', '#', ' '], [' ', '#', '#', ' '], ['#', ' ', '#', ' '], [' ', ' ', '#', ' '], [' ', ' ', '#', ' '], [' ', '#', '#', '#']]
a2 = [[' ', '#', '#', ' '], ['#', ' ', ' ', '#'], [' ', ' ', '#', ' '], [' ', '#', ' ', ' '], ['#', ' ', ' ', ' '], ['#', '#', '#', '#']]
a3 = [['#', '#', '#', ' '], [' ', ' ', ' ', '#'], ['#', '#', '#', ' '], [' ', ' ', ' ', '#'], [' ', ' ', ' ', '#'], ['#', '#', '#', ' ']]
a4 = [['#', ' ', ' ', ' '], ['#', ' ', ' ', '#'], ['#', '#', '#', '#'], [' ', ' ', ' ', '#'], [' ', ' ', ' ', '#'], [' ', ' ', ' ', '#']]
a5 = [['#', '#', '#', '#'], ['#', ' ', ' ', ' '], ['#', '#', '#', ' '], [' ', ' ', ' ', '#'], [' ', ' ', ' ', '#'], ['#', '#', '#', ' ']]
a6 = [[' ', '#', '#', '#'], ['#', ' ', ' ', ' '], ['#', '#', '#', ' '], ['#', ' ', ' ', '#'], ['#', ' ', ' ', '#'], [' ', '#', '#', ' ']]
a7 = [['#', '#', '#', '#'], [' ', ' ', ' ', '#'], [' ', ' ', '#', ' '], [' ', '#', ' ', ' '], ['#', ' ', ' ', ' '], ['#', ' ', ' ', ' ']]
a8 = [[' ', '#', '#', ' '], ['#', ' ', ' ', '#'], [' ', '#', '#', ' '], [' ', '#', '#', ' '], ['#', ' ', ' ', '#'], [' ', '#', '#', ' ']]
a9 = [[' ', '#', '#', ' '], ['#', ' ', ' ', '#'], ['#', ' ', ' ', '#'], [' ', '#', '#', '#'], [' ', ' ', ' ', '#'], ['#', '#', '#', ' ']]
a0 = [[' ', '#', '#', ' '], ['#', ' ', ' ', '#'], ['#', '#', ' ', '#'], ['#', ' ', '#', '#'], ['#', ' ', ' ', '#'], [' ', '#', '#', ' ']]
aa = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

numbers = {'1':a1, '2':a2, '3':a3, '4':a4, '5':a5, '6':a6, '7':a7, '8':a8, '9':a9, '0':a0}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def time_in_num():
    what_time = time.strftime('%H%M%S')
    hour0 = numbers[what_time[0]]
    hour1 = numbers[what_time[1]]
    minute0 = numbers[what_time[2]]
    minute1 = numbers[what_time[3]]
    second0 = numbers[what_time[4]]
    second1 = numbers[what_time[5]]
    
    printing_time_table = []
    n = 0
    while n < 6:
        printing_time_table.append(hour0[n] + hour1[n] + aa[n] + minute0[n] + minute1[n] + aa[n] + second0[n] + second1[n])
        n+=1
    return printing_time_table

def print_clock():
    while True:
        clear()
        time_table = time_in_num()
        rowsnumb, columns = os.popen('stty size', 'r', 1).read().split()
        centercol = (' ' * int(((int(columns)) - 63) // 2))
        rowcenter = ('\n' * int(((int(rowsnumb)) - 7) // 2))
        print(rowcenter)
        for rows in time_table:
            rows.insert(0, centercol)
            print(' '.join(rows))
        time.sleep(1)

print_clock()
