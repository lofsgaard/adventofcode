def main():
    compare(get_input())


prio = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
        'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
        'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
        'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
        'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33,
        'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
        'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47,
        'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}


def compare(items):
    total = []
    chunk_size = 3
    for i in range(0, len(items), chunk_size):
        chunk = items[i:i + chunk_size]
        comp1, comp2, comp3 = chunk[0], chunk[1], chunk[2]
        chars = list(set(comp1) & set(comp2) & set(comp3))
        for i in chars:
            total.append(prio[i])
    print(sum(total))


def get_input():
    with open('inputday3.txt') as f:
        lines = f.readlines()
        list_lines = []
        for line in lines:
            list_lines.append(line.rstrip('\n'))
        return list_lines


main()
