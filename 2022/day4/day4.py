def main():
    compare(get_input())


def compare(items):
    sections = []
    counter = 0
    counter = 0
    for x in items:
        sections.append(x.split(','))
    for line in sections:
        int1 = int(line[0].split('-')[0])
        int2 = int(line[0].split('-')[1])
        int3 = int(line[1].split('-')[0])
        int4 = int(line[1].split('-')[1])
        #print(int1, int2)
        #print(int3, int4)

        start = range(int1, int2).start in range(int3, int4)
        stop = range(int1, int2).stop in range(int3, int4)
        #print(start, stop)
        if fullrange1 or fullrange2:
            counter = counter +1
    print(counter)


def get_input():
    with open('inputday4.txt') as f:
        lines = f.readlines()
        list_lines = []
        for line in lines:
            list_lines.append(line.rstrip('\n'))
        return list_lines


main()
