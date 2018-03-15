import os
import pickle
import argparse
from sys import stdin


def line_handling(line, d, args):     # обработка строки
    string = list(line.split())
    firstword = ""
    for word in string:
        secondword = ""
        if args.ls:
            word = word.lower()
        control = 0
        for j in word:      # проверка на принадлежность русскому алфавиту
            if ord(j) >= 1040 and ord(j) <= 1103:
                secondword += j
                control += 1        # проверка, что в слове есть русская буква
        if control > 0 and firstword != "":
            if firstword not in d:
                d[firstword] = dict()
                d[firstword][secondword] = 1
            else:
                if secondword in d[firstword]:
                    d[firstword][secondword] += 1
                else:
                    d[firstword][secondword] = 1
        firstword = secondword


parser = argparse.ArgumentParser(description='A script which collects words from file')
parser.add_argument('--input-dir', dest='file', type=str, default='stdin', help='File directory')
parser.add_argument('--model', type=str, help='Save directory')
parser.add_argument('--ls', action='store_true', help='Switch to lowercase')
args = parser.parse_args()
d = dict()
if args.file == 'stdin':
    for line in stdin:
        line_handling(line, d, args)
else:
    f = open(args.file)
    for line in f:
        line_handling(line, d, args)
z = open('C://Users/mert-/Desktop/txtgener/project/dic_module.txt', 'w')
for index in d:
    z.write(index + ' - ' + str(d[index]) + '       ')
with open('d.pickle', 'wb') as args.model:
    pickle.dump(d, args.model)