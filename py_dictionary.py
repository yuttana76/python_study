phonebook = {
    'John':999,
    'Jack':888,
    'Jill':777
}
print(phonebook)

#Interating
for name,tel in phonebook.items():
    print('%s has phone number is %s' %(name,tel))

#Delete item
print('Delete item')
del phonebook['Jill']
print(phonebook)

#Update and Add item
print('Update and Add item')
phonebook.update({'AAA':222})
phonebook.update({'Jack':555})
print(phonebook)

if "Jill" in phonebook:
    print('Hi Jack your phone number is %s' %(phonebook['Jack']) )
