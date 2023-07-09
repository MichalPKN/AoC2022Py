import functools
import copy

input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

f = open("AoC2022\\adv13.txt", "r")
input = f.read().rstrip()

# input = """[[], [8, 5, 9], [[[5], [3]], 7, 4, 4], [8]]
# [[], [8,5,9]]"""

# input = """[[1],[2,3,4]]
# [[1],4]"""

input = input.split("\n\n")

def arrayCompare(a, b):
    for i in range(len(a)):
        if len(b) == i:
            return -1
        if isinstance(a[i], int):
            if isinstance(b[i], int):
                if a[i] > b[i]:
                    return -1
                elif b[i] > a[i]:
                    return 1
            else:
                a[i] = [a[i]]
                tmp = arrayCompare(a[i], b[i])
                if tmp != 0:
                    return tmp
        else:
            if isinstance(b[i], int):
                b[i] = [b[i]]
            tmp = arrayCompare(a[i], b[i])
            if tmp != 0:
                return tmp
    if a == [] and b != []:
        return 1
    return 0

def compare(a, b):
    c = copy.deepcopy(a)
    d = copy.deepcopy(b)
    tmp = arrayCompare(c, d)
    if tmp == 1 or tmp == 0:
        return -1
    else:
        return 1
        
data = []
for line in input:
    line = line.split("\n")
    data.append(eval(line[0]))
    data.append(eval(line[1]))
data.append([[2]])
data.append([[6]])
data = sorted(data, key=functools.cmp_to_key(compare))
for i in range(len(data)):
    if [[2]] == data[i]:
        idk1 = i+1
        print(i+1)
        print(data[i])
    if [[6]] == data[i]:
        idk2 = i+1
        print(i+1)
        print(data[i])
print(idk1 * idk2)


#part 1

# sum = 0
# for i in range(len(input)):
#     input[i] = input[i].split("\n")
#     a=[]
#     aN = 0
#     input[i][0] = eval(input[i][0])
#     input[i][1] = eval(input[i][1])
#     tmp = compare(input[i])
#     if tmp == 1:
#         sum += i + 1

# print(sum)