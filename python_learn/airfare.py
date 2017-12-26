age = int(input('How Old are you?'))
if age <= 2:
    print(' free')
elif 2 < age < 13:
    print(' child fare')
else:
    print('adult fare')

food = input("What's your favorite food?")
reply = 'yuck' if food == 'lamb' else 'back'
print(reply)