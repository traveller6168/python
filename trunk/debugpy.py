#!usr/bin/python3
import string
alphas = string.ascii_letters+'_'
nums = string.digits

print ('Wecome to the Identifier Checker v1.0')
print ('Testees must be at least 2 chars long.')

myInput = input('Indentifier to test?')
if len(myInput) > 1:
    if myInput[0] not in alphas:
        print('''invalid: first symbol must bi alphabetic''')
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print('''invalid:remaining symbols must be alphabetic''')
                break
            else:
               print("okay as an identifier")
else:
    print('length is not engouth')