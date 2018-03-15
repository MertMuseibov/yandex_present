import pickle
import random
import argparse
from sys import stdin


def rand_choose(dic, word, result, args):
    a = []
    for neighboring in dic[word]:
        a.append(neighboring)
    current = random.choice(a)
    if args.file == 'stdout':
        print(current + ' ', end='')
    else:
        result.write(current + ' ')
    return current


parser = argparse.ArgumentParser(description='A script which collects words from file')
parser.add_argument('--model', type=str, help='Load dictionary from a file')
parser.add_argument('--seed', dest='first', type=str, help='First word')
parser.add_argument('--length', type=int, help='The length of the generated text')
parser.add_argument('--output', dest='file', type=str, default='stdout', help='Finished text download file')
args = parser.parse_args()
f = args.model    # откуда будем выгружать словарь
with open('d.pickle', 'rb') as f:
    my_dic = pickle.load(f)
first = args.first
length = args.length
way = args.file
result = open(way, 'w')
current = first
for i in range(length):
    if current in my_dic:
        current = rand_choose(my_dic, current, result, args)
    else:
        a = []
        for key in my_dic:
            a.append(key)
        current = random.choice(a)
        if args.file == 'stdout':
            print(current + ' ', end='')
        else:
            result.write(current + ' ')