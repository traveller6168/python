for i in range(10, 11):
    print(i+1)
    if i/2 == 1:
        print(i)
    elif i/3 != 1:
        print(i/3)

print('ceshi')

for j in range(3, 0, -1):
    while j > 0:
        print(j)
        j = j - 1

print('new test')

n = int(input('Enter an integer >= 0:'))
fact = 1
for i in range(2, n + 1):
    fact = fact * i
print(str(n) + ' factorial is ' + str(fact))

n = int(input('How many numbers to sum?'))
total = 0
for m in range(n):
    s = input('Enter number ' + str(m+1) + ' is :')
    total = total + int(s)
print('The sum is ' + str(total))

total = 0
s = input('Enter a number (or "done"): ')
while s != 'done':
    num = int(s)
    total = total + num
    s = input('Enter a number (or "dend"): ')
print('The su is ' + str(total))
