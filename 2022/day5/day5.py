def main():
    move_items(get_input())
    #get_last_item()


crates = {
    '1': ['R', 'P', 'C', 'D', 'B', 'G'],
    '2': ['H', 'V', 'G'],
    '3': ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
    '4': ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
    '5': ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
    '6': ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
    '7': ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
    '8': ['C', 'M', 'D', 'B', 'F'],
    '9': ['F', 'C', 'Q', 'G']
}

cratestest = {
    '1': ['Z', 'N'],
    '2': ['M', 'C', 'D'],
    '3': ['P']
}


def move_items(string):
    instruction = []
    for i in string:
        instruction.append(i.lstrip('move ').split(' '))

    for item in instruction:
        item.remove('from')
        item.remove('to')

    for line in instruction:
        for x in range(int(line[0])):
            print(f'Move {int(line[0])} items from {int(line[1])} to {int(line[2])}')






def get_last_item():
    for key, val in cratestest.items():
        for i in key:
            print(val[-1], end='')


def get_input():
    with open('inputday5test.txt') as f:
        lines = f.readlines()
        list_lines = []
        for line in lines:
            list_lines.append(line.rstrip('\n'))
        return list_lines


main()


