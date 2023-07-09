input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

f = open("AoC2022\\adv1.txt", "r")
input = f.read().rstrip()

input = input.split("\n\n")
for i in range(len(input)):
    input[i] = input[i].split("\n")
    total = 0
    for calo in input[i]:
        total += int(calo)
    input[i] = total
max = [0,0,0]
for j in range(len(max)):
    for total in input:
        if total > max[j] and total not in max:
            max[j] = total
print(max[0] + max[1] + max[2])

