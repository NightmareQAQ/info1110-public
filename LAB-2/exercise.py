print('Input 3 strings and find what string is the longest')
names = []
name_1 = input()
name_2 = input()
name_3 = input()
names.append(name_1)
names.append(name_2)
names.append(name_3)
long = 0
longest_name = ''
if len(name_1) == len(name_2) == len(name_3):
    if len(name_1) != 0:
        print('All strings are the same length')
        exit()

for i in names:
    check_num = len(i)
    if len(i) > long:
        long = len(i)
        longest_name = i

if long > 0:
    print('"{}" is the longest string'.format(longest_name))
elif long == 0:
    print('All strings are empty')
else:
    print('invalid input')




