firstName = input('Enter the first name:')
lastName = input('Enter the last name:')
zipCode = input('Enter the ZIP code:')
id = input('Enter an employee ID:')

if not (len(firstName) >= 2 and firstName.isalpha()):
    if len(firstName) == 0:
        print('The first name must be filled in.')
    else:
        print('"{}" is not a valid first name.'.format(firstName), end="")
        if len(firstName) == 1 and firstName.isalpha():
            print(' It is too short.')

if not (len(lastName) >= 2 and lastName.isalpha()):
    if len(lastName) == 0:
        print('The last name must be filled in.')
    else:
        print('"{}" is not a valid last name.'.format(lastName), end="")
        if len(lastName) == 1 and lastName.isalpha():
            print(' It is too short.')

if not zipCode.isdigit():
    print('The ZIP code must be numeric.')

if not (id[0:2].isalpha() and id[2] == '-' and id[3:].isdigit() and len(id) == 7):
    print('{} is not a valid ID.'.format(id))