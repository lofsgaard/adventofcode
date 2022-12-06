def main():
    get_input()


def get_input():
    with open('inputday3.txt') as f:
        lines = f.readlines()
        list_lines = []
        for line in lines:
            list_lines.append(line.rstrip('\n'))
        return list_lines


main()
