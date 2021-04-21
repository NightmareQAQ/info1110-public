import random
right = ''
for i in range(4):
    if i <= 4:
        n = random.randint(1, 9)
        right = right + str(n)
print(right)
