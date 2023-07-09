input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

f = open("AoC2022\\adv4.txt", "r")
input = f.read().rstrip()

input = input.split("\n")
totalOverlap=0
for line in input:
    line = line.split(",")
    line[0] = line[0].split("-")
    line[1] = line[1].split("-")
    # part 1
    # if((int(line[0][0])<=int(line[1][0]) and int(line[0][1])>=int(line[1][1])) or (int(line[0][0])>=int(line[1][0]) and int(line[0][1])<=int(line[1][1]))):
    #     totalOverlap += 1
    overlaps = 0
    for i in range(int(line[0][0]),int(line[0][1])+1):
        for j in range(int(line[1][0]), int(line[1][1])+1):
            if i == j:
                overlaps = 1
    totalOverlap += overlaps
print(totalOverlap)