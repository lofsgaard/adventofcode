def main():
    games(get_input())

def get_input():
    with open('inputday2.txt') as f:
        lines = f.readlines()
        list_lines = []
        for line in lines:
            list_lines.append(line.rstrip('\n'))
        return list_lines


def games(input):
    # Rock/A/X = 1 Paper/B/Y = 2 Scissord/C/Z = 3
    score = []
    for i in input:
        game = i.split(' ')
        print(game)
        if game[0] == 'A' and game[1] == 'X':
            #Lose
            score.append(3)
        elif game[0] == 'A' and game[1] == 'Y':
            #Draw
            score.append(4)
        elif game[0] == 'A' and game[1] == 'Z':
            #Win
            score.append(8)
        elif game[0] == 'B' and game[1] == 'X':
            #Lose
            score.append(1)
        elif game[0] == 'B' and game[1] == 'Y':
            #Draw
            score.append(5)
        elif game[0] == 'B' and game[1] == 'Z':
            #Win
            score.append(9)
        elif game[0] == 'C' and game[1] == 'X':
            #Lose
            score.append(2)
        elif game[0] == 'C' and game[1] == 'Y':
            #Draw
            score.append(6)
        elif game[0] == 'C' and game[1] == 'Z':
            #Win
            score.append(7)
        else:
            print("something wrong")
    print(sum(score))
            
main()