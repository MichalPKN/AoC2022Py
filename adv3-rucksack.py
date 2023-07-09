input="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

f = open("AoC2022\\adv3.txt", "r")
input = f.read().rstrip()

input = input.split("\n")
letters = []
for i in range(0,len(input),3):
    theLetter = ""
    for letter in input[i]:
        if letter in input[i+1]:
            theLetter += letter
    for letter in theLetter:
        if letter in input[i+2]:
            theLetter = letter
    letters.append(theLetter)
print(letters)
sum=0
for char in letters:
    if char.isupper():
        sum += ord(char)-64+26
    else:
        sum += ord(char)-96
print(sum)