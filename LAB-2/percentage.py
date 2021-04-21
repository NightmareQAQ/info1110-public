percent = 12.3456789
mb = 4100
message = 'process: {:.2f}% , {:06d} MB '.format(percent, mb)
print(message)
# print('{:06.2f}'.format(3.141592653589793))

print('\n percent: {:.2%}'.format(12.3456789))
print('percent: {:.2f}%'.format(12.3456789))
print('mb: {:066d}'.format(666))
