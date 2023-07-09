input = """A Y
B X
C Z"""

f = open("AoC2022\\adv2.txt", "r")
input = f.read().rstrip()

input = input.split("\n")

score = 0
for game in input:
    game = game.split(" ")
    if game[1] == 'X':
        if game[0] == 'A':
            score += 3
        elif game[0] == 'B':
            score += 1
        elif game[0] == 'C':
            score += 2
    elif game[1] == 'Y':
        if game[0] == 'A':
            score += 4
        elif game[0] == 'B':
            score += 5
        elif game[0] == 'C':
            score += 6
    elif game[1] == 'Z':
        if game[0] == 'A':
            score += 8
        elif game[0] == 'B':
            score += 9
        elif game[0] == 'C':
            score += 7
print(score)