input="""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

f = open("AoC2022\\adv10.txt", "r")
input = f.read().rstrip()

input = input.split("\n")

cycles = 0
x = 1 #pos of middle x of 3

for cycle in input:
    cycles += 1
    if cycles in [x, x+1, x+2]:
        print('# ', end="")
    else:
        print('. ', end="")
    if cycles % 40 == 0:
        print()
        cycles = 0
    if "addx" in cycle:
        cycles += 1
        cycle = cycle.split(" ")
        if cycles in [x, x+1, x+2]:
            print('# ', end="")
        else:
            print('. ', end="")
        if cycles % 40 == 0:
            print()
            cycles = 0
        x += int(cycle[1])


#part 1

# for cycle in input:
#     if cycle == "noop":
#         cycles += 1
#         if (cycles-20) % 40 == 0:
#             sum += cycles * x
#     else:
#         cycle = cycle.split(" ")
#         cycles += 1
#         if (cycles-20) % 40 == 0 and cycles != 0:
#             sum += cycles * x
#         cycles += 1
#         if (cycles-20) % 40 == 0:
#             sum += cycles * x
#         x += int(cycle[1])
# print(sum)
    