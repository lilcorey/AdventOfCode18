# read inputs into a list, converting from str to int
fp = open('input.txt')
inputs = []
for line in fp.readlines():
  inputs.append(int(line))

# Pt. 1
total = sum(inputs)
print(f'resulting Freq {total}')

# Pt. 2
# Could use itertools.cycle to cycle a list indefinitely and then break when condition is met
# Set could also be used
dic = {}
total = 0
while True:
  for line in inputs:
    total += int(line)
    if total in dic:
      print(f'loop found {total}'); exit()
    dic[total] = True