input = """30373
25512
65332
33549
35390"""

f = open("AoC2022\\adv8.txt", "r")
input = f.read().rstrip()

input = input.split("\n")

maxScore = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        score = 1
        treesSeen = 0
        for left in range(j-1,-1,-1):
            if input[i][left]>=input[i][j]:
                treesSeen += 1
                break
            else:
                treesSeen += 1
        if treesSeen:
            score *= treesSeen
        treesSeen = 0
        for up in range(i-1,-1,-1):
            if input[up][j]>=input[i][j]:
                treesSeen += 1
                break
            else:
                treesSeen += 1
        if treesSeen:
            score *= treesSeen
        treesSeen = 0
        for right in range(j+1, len(input[j])):
            if input[i][right]>=input[i][j]:
                treesSeen += 1
                break
            else:
                treesSeen += 1
        if treesSeen:
            score *= treesSeen
        treesSeen = 0
        for down in range(i+1, len(input[i])):
            if input[down][j]>=input[i][j]:
                treesSeen += 1
                break
            else:
                treesSeen += 1
        if treesSeen:
            score *= treesSeen
        if score > maxScore:
            maxScore = score
print(maxScore)


# first part

# totalSeen = 0
# for i in range(len(input)):
#     for j in range(len(input[i])):
#         seen = True
#         for left in range(j):
#             if input[i][left]>=input[i][j]:
#                 seen = False
#                 break
#         if seen:
#             totalSeen += 1
#             #print(input[i][j], i, j)
#             continue
#         else:
#             seen = True
#             for up in range(i):
#                 if input[up][j]>=input[i][j]:
#                     seen = False
#                     break
#             if seen:
#                 totalSeen += 1
#                 #print(input[i][j], i, j)
#                 continue
#             else:
#                 seen = True
#                 for right in range(len(input[j])-1, j, -1):
#                     if input[i][right]>=input[i][j]:
#                         seen = False
#                         break
#                 if seen:
#                     totalSeen += 1
#                     #print(input[i][j], i, j)
#                     continue
#                 else:
#                     seen = True
#                     for down in range(len(input[i])-1, i, -1):
#                         if input[down][j]>=input[i][j]:
#                             seen = False
#                             break
#                     if seen:
#                         totalSeen += 1
#                         #print(input[i][j], i, j)
#                         continue
# print(totalSeen)
                
                