s = 'Hello World!'

for c in s:
    print(ord(c), end=' ')
print()

print([ord(c) for c in s])

print(list(map(ord, s)))

str_sum = 0
for c in s:
    str_sum += ord(c)
print('Sum is: %d' % str_sum)

print('Sum is: {}'.format(sum(map(ord, s))))
