input="""mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

f = open("AoC2022\\adv6.txt", "r")
input = f.read().rstrip()

for i in range(len(input)):
    setArr = set()
    for j in range(14):
        setArr.add(input[i+j])
        if len(setArr) == 14:
            print(i+14)
            print(setArr)
            exit()