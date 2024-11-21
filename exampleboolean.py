first= input('Enter your first name: ')
print('Hello', first)
if first == 'John':
    print(first, 'is learning python')
elif first == 'Jack':
    print(first, 'is learning with fellow students in the community')
else:
    # This is just in case we have a younger user who can't yet read
    age = int(input('How old are you?  '))
    if age <= 6:
        print('Wow you are {}! if you are confident with your reading already....'.format(age))
    print('{} you should totally learn python'.format(first))
print('Have a great day {}!'.format(first))
