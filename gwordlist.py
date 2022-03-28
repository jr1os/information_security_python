import itertools


def gw(string):
    result = itertools.permutations(string, 3)
    for e in result:
        print(''.join(e))


if __name__ == "__main__":
    print(gw('abc'))
