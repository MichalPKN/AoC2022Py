input="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

f = open("AoC2022\\adv5.txt", "r")
input = f.read().rstrip()

input = input.split("\n\n")
numberOfSlopes = 9 #change to 3 for test
slopes = [[],[],[],[],[],[],[],[],[]] #change to [[],[],[]] for test
cargo = input[0].split("\n")
for i in range(len(cargo)-1):
    for j in range(numberOfSlopes):
        if cargo[i][j*4+1] != ' ':
            slopes[j].append(cargo[i][j*4+1])
print(slopes)
for line in input[1].split("\n"):
    line = line.split(" ")
    pickedUp=[]
    for i in range(int(line[1])):
        pickedUp.insert(0, slopes[int(line[3])-1][0])
        slopes[int(line[3])-1].pop(0)
    for i in pickedUp:
        slopes[int(line[5])-1].insert(0, i)
for crates in slopes:
    print(crates[0], end = "")
print()