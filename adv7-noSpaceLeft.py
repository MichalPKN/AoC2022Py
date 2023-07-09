input="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

f = open("AoC2022\\adv7.txt", "r")
input = f.read().rstrip()

input = input.split("\n")
dirs = {}
currDirs = []
for line in input:
    line = line.split()
    #print(line)
    if line[0] == '$':
        if line[1] == 'cd':
            #print(line, currDirs)
            if line[2] == '..':
                currDirs.pop()
            else:
                currDirs.append(line[2])
                #dirs.setdefault(line[2],0)
                path = ""
                for j in currDirs:
                    path += j
                dirs.update({path:0})
    elif line[0] != 'dir':
        print(currDirs)
        for i in range(len(currDirs)):
            path=""
            for j in currDirs[:(i+1)]:
                    path += j
            dirs[path] += int(line[0])
min = 70000000
print(30000000 - (70000000 - dirs['/']), dirs['/'], (70000000 - dirs['/']))
spaceNeed = 30000000 - (70000000 - dirs['/'])
for key,i in dirs.items():
    if i > spaceNeed and i < min:
        #print(key, i)
        min = i
print(min)
print(dirs)


# part 1

# #print(dirs)
# sum = 0
# for key,i in dirs.items():
#     if i <= 100000:
#         #print(key, i)
#         sum += i
# print(sum)
