input="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


f = open("AoC2022\\adv11.txt", "r")
input = f.read().rstrip()


input = input.split("\n\n")
items = []
inspects = []
operations = []
divisibles = []
monkeys = []
for i in range(len(input)):
    input[i] = input[i].split("\n")
    items.append([])
    inspects.append(0)
    input[i][1] = input[i][1].replace("Starting items: ", "")
    for item in input[i][1].split(", "):
        items[i].append(int(item))
    operations.append(input[i][2].replace("  Operation: new = old ", "").split(" "))
    divisibles.append(int(input[i][3].replace("  Test: divisible by ", "")))
    monkeys.append([int(input[i][4].replace("    If true: throw to monkey ", "")), int(input[i][5].replace("    If false: throw to monkey ", ""))])
    
for n in range(20):
    for i in range(len(input)):
        for j in range(len(items[i])):
            if operations[i][1] == "old":
                item = items[i][0] * items[i][0]
            elif operations[i][0] == '*':
                item = items[i][0] * int(operations[i][1])
            elif operations[i][0] == '+':
                item = items[i][0] + int(operations[i][1])
            item = item // 3
            if item % divisibles[i] == 0:
                items[monkeys[i][0]].append(item)
            else:
                items[monkeys[i][1]].append(item)
            items[i].pop(0)
            inspects[i] += 1
print(inspects)
print(sorted(inspects)[-1] * sorted(inspects)[-2])
# 243*236=57348