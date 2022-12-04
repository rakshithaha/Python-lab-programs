birthdays = {'SINCHANA': '2nd aug,2002', 'PRATHAMA': '18th june,2002', 'SAGARIKA': '1st july,2002', 'SANJANA': '26th feb,2002', 'SPOORTHI': '21st sep,2002'}
while True:
    name = input("Enter name:(or leave a blank to quit) \n").upper()
    if name == '':
        print('NO NAME ENTERED')
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('THE NAME YOU ENTERED IS NOT IN THE BIRTHDAYS DATABASE')
        print('-----------------------------------------------------')
        print('Anyways,you can still add it to the DATABASE')
        print('What is their birthday? (or enter to quit)')
        bday = input()
        if bday == '':
            break
        else:
            birthdays[name] = bday
            print('BIRTHDAYS DATABASE NOW UPDATED!!!')
