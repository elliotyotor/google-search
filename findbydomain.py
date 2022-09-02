
from googlesearch import search
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, required=True)
parser.add_argument('--q', type=str, required=True)
args = parser.parse_args()
f = open("result.txt", "w")
for i in search(args.q, stop=args.n, pause=2):
    if args.q in i:
        f.write(i+"\n")
f.close()