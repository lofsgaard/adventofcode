def main():
    compare(get_input())


def compare(items):
    sections = []
    counter = 0
    counter = 0
    for x in items:
        sections.append(x.split(','))
    for line in sections:
        start = range(int(line[0].split('-')[0]), int(line[0].split('-')[1])).start in \
                range(int(line[1].split('-')[0]), int(line[1].split('-')[1]))

        stop = range(int(line[0].split('-')[0]), int(line[0].split('-')[1])).stop in \
               range(int(line[1].split('-')[0]), int(line[1].split('-')[1]))
        print(start, stop)
        if stop or start:
            counter = counter + 1
    print(counter)





def get_input():
    with open('inputday4test.txt') as f:
        lines = f.readlines()
        list_lines = []
        for line in lines:
            list_lines.append(line.rstrip('\n'))
        return list_lines


main()