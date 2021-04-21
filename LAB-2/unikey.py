import random
name_1 = input('Enter your Full name: ')
name_2, name_3 = name_1.split(' ', 1)
# print(name_2)
# print(name_3)
lift = name_2[0].lower() + name_3[0].lower() + name_3[1] + name_3[2]
# right = int(random.randint(1, 9) + random.randint(1, 9) + 1 + 2)
# print(right)
#for i in range(4):
#  if i <= 4:
#     right = input(random.randint(1, 9))
#    i += 1
right = ''
for i in range(4):
    if i <= 4:
        n = random.randint(1, 9)
        right = right + str(n)

print(lift + str(right))
