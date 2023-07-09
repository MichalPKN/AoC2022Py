input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

f = open("AoC2022\\adv12.txt", "r")
input = f.read().rstrip()

input = input.split("\n")
nmap = [[9999 for x in range(len(input[0]))] for y in range(len(input))]
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'E':
            starty = i
            startx = j
        if input[i][j] == 'S':
            input[i] = input[i][:j] + 'a' + input[i][(j+1):]
nmap[starty][startx] = 0
while(True):
    min = 10000
    minx = 0
    miny = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if nmap[i][j] < min and nmap[i][j] != -1:
                min = nmap[i][j]
                minx = j
                miny = i 
    char = input[miny][minx]
    if char == 'a':
        e = min
        break
    if char == 'E':
        char = 'z'
    maxChar = ord(char) - 1
    if minx + 1 < len(input[0]) and ord(input[miny][minx+1]) >= maxChar and nmap[miny][minx+1] > nmap[miny][minx] + 1:
        nmap[miny][minx + 1] = nmap[miny][minx] + 1
    if minx - 1 >= 0 and ord(input[miny][minx-1]) >= maxChar and nmap[miny][minx-1] > nmap[miny][minx] + 1:
        nmap[miny][minx - 1] = nmap[miny][minx] + 1
    if miny - 1 >= 0 and ord(input[miny-1][minx]) >= maxChar and nmap[miny-1][minx] > nmap[miny][minx] + 1:
        nmap[miny-1][minx] = nmap[miny][minx] + 1
    if miny + 1 < len(input) and ord(input[miny+1][minx]) >= maxChar and nmap[miny+1][minx] > nmap[miny][minx] + 1:
        nmap[miny+1][minx] = nmap[miny][minx] + 1
    nmap[miny][minx] = -1

print(e)


#part 2

# input = input.split("\n")
# nmap = [[9999 for x in range(len(input[0]))] for y in range(len(input))]
# for i in range(len(input)):
#     for j in range(len(input[0])):
#         if input[i][j] == 'S':
#             starty = i
#             startx = j
#         if input[i][j] == 'E':
#             input[i] = input[i][:j] + 'z' + input[i][(j+1):]
#             endy = i
#             endx = j
# nmap[starty][startx] = 0
# while(True):
#     min = 10000
#     minx = 0
#     miny = 0
#     for i in range(len(input)):
#         for j in range(len(input[0])):
#             if nmap[i][j] < min and nmap[i][j] != -1:
#                 min = nmap[i][j]
#                 minx = j
#                 miny = i 
#     char = input[miny][minx]
#     if minx == endx and miny == endy:
#         e = min
#         break
#     if char == 'S':
#         char = 'a'
#     maxChar = ord(char) + 1
#     if minx + 1 < len(input[0]) and ord(input[miny][minx+1]) <= maxChar and nmap[miny][minx+1] > nmap[miny][minx] + 1:
#         nmap[miny][minx + 1] = nmap[miny][minx] + 1
#     if minx - 1 >= 0 and ord(input[miny][minx-1]) <= maxChar and nmap[miny][minx-1] > nmap[miny][minx] + 1:
#         nmap[miny][minx - 1] = nmap[miny][minx] + 1
#     if miny - 1 >= 0 and ord(input[miny-1][minx]) <= maxChar and nmap[miny-1][minx] > nmap[miny][minx] + 1:
#         nmap[miny-1][minx] = nmap[miny][minx] + 1
#     if miny + 1 < len(input) and ord(input[miny+1][minx]) <= maxChar and nmap[miny+1][minx] > nmap[miny][minx] + 1:
#         nmap[miny+1][minx] = nmap[miny][minx] + 1
#     nmap[miny][minx] = -1
#     # for line in range(len(nmap)):
#     #     for num in range(len(nmap[line])):
#     #         print("{0:4d}".format(nmap[line][num]), end=input[line][num]+" ")
#     #     print()
#     # print()


# # for line in range(len(nmap)):
# #     for num in range(len(nmap[line])):
# #         print("{0:4d}".format(nmap[line][num]), end=input[line][num])
# #     print()

# print(e)



#get lowest path posi
    # check around
        # if same letter or one bigger
            # if curr path > next path
                # change path to new
