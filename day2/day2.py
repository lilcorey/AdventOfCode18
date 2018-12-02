# read inputs into a list
fp = open('input.txt')
inputs = []
for line in fp.readlines():
  inputs.append(line.strip().split('\n')[0])

# Pt. 1
twos = threes = 0

# create dict of frequencies for each letter in ID
for line in inputs:
  dic = {}
  for c in line:
    if c in dic:
      dic[c] += 1
    else:
      dic[c] = 1

  # increment counters if pairs of 2 or 3
  if 2 in dic.values():
    twos += 1
  if 3 in dic.values():
    threes += 1

print(f'{twos} x {threes} = {twos*threes}')

# Pt. 2
# O(n^2) compare each line w/ every other
for line in inputs:
  for nextLine in inputs:
    dif = 0
    for i,c in enumerate(line):
      if c != nextLine[i]:
        dif += 1
    if dif == 1:
      ans = [c for i, c in enumerate(line) if c == nextLine[i]]
      ans = ''.join(ans)
      print(f'{line}\n{nextLine} = {ans}'); exit()
