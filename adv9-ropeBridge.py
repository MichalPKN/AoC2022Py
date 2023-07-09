input="""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

f = open("AoC2022\\adv9.txt", "r")
input = f.read().rstrip()


input = input.split("\n") 

grid = {(0,0)}
rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for move in input:  
    move = move.split(" ")
    for i in range(int(move[1])):
        if move[0] == "R":
            rope[0][0] += 1
        elif move[0] == "D":
            rope[0][1] -= 1
        elif move[0] == "L":
            rope[0][0] -= 1
        elif move[0] == "U":
            rope[0][1] += 1
        for k in range(len(rope)-1):
            if (rope[k][0] - rope[k+1][0] >= 2):
                rope[k+1][0] += 1
                if (rope[k][1] - rope[k+1][1] >= 1):
                    rope[k+1][1] +=1
                elif (rope[k][1] - rope[k+1][1] <= -1):
                    rope[k+1][1] -=1 
            elif (rope[k][0] - rope[k+1][0] <= -2):
                rope[k+1][0] -= 1
                if (rope[k][1] - rope[k+1][1] >= 1):
                    rope[k+1][1] +=1
                elif (rope[k][1] - rope[k+1][1] <= -1):
                    rope[k+1][1] -=1 
            if (rope[k][1] - rope[k+1][1] >= 2):
                rope[k+1][1] +=1
                if (rope[k][0] - rope[k+1][0] >= 1):
                    rope[k+1][0] +=1
                elif (rope[k][0] - rope[k+1][0] <= -1):
                    rope[k+1][0] -=1 
            elif (rope[k][1] - rope[k+1][1] <= -2):
                rope[k+1][1] -=1
                if (rope[k][0] - rope[k+1][0] >= 1):
                    rope[k+1][0] +=1
                elif (rope[k][0] - rope[k+1][0] <= -1):
                    rope[k+1][0] -=1 
        grid.add((rope[9][0], rope[9][1]))
    #print(rope)
print(grid)
print(len(grid))