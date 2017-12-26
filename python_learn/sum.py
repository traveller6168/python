from learn import area as area

total = 0
while True:
    s = input('Enter a number (or "done"): ')
    if s == 'done':
        break
    num = int(s)
    total = total + num
print('The sum is ' + str(total))

for row in range(1, 3):
    for col in range(1, 3):
        prod = row * col
        if prod < 3:
            print(' ', end = '')
        print(row * col, ' ', end = '')
    print()


x = pow(2, 3)
print(x)

y = area.area(7)*9+10
print(y)
print(area.area.__doc__)