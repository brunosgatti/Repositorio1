#!/usr/bin/env python3


print('1. For the next series of tasks about lists, use the interpreter')

print('\na. Create a list of 5 of your favorite things.')
favs = ['limão', 'banana', 'abacaxi', 'mamão', 'tangerina']

print('\nb. Use the print() function to print your list.')
print(favs)

print('\nc. Use the print() function to print out the middle element.')
print('The middle element is', favs[2])

print('\nd. Now replace the middle element with a different item, your favorite song, or song bird.')
favs[2] = 'Gimme chocolate!!'

print('\ne. Use the same print statement from b. to print your new list. Check out the differences:', '\n', favs, '-As you can see, I replaced abacaxi with Gimme chocolate!!')

print('\nf. Add a new element to the end.')
favs.append('maçã')
print('g. Add a new element to the beginning')
favs.insert(0,'uva')
print('h. Add a new element somewhere other than the beginning or the end.')
favs.insert(5,'manga')
print('Now, printing the list based on the changes from f., g. and h.:', '\n', favs)

print('\ni. Remove an element from the end.')
favs.pop()
print('j. Remove and element from the beginning')
favs.pop(1)
print('k. Reove an element from somewhere other than the beginning or the end.')
favs.pop(3)
print('Now, printing the list based on the changes from i., j. and k.:', '\n', favs)

print('\nl. Use join to create a string. Join the elements on','.')
text = ['Socorram-me', 'subi', 'no', 'ônibus', 'em', 'Marrocos']
print(' '.join(text))

print('\n')

print('2.Write a script that splits a string into a list. In your script:')

print('-Save the string "sapiens, erectus, neanderthalensis" as a variable named taxa')
taxa = 'sapiens, erectus, neanderthalensis'

print('\n-Print taxa')
print(taxa)

print('\n-Print taxa[1]. What do you get?')
print('Printing taxa[1], we get:', taxa[1])

print('\n-Print type[taxa]. What is its type?')
print('Its type is', type(taxa))

print('\n-Split taxa into individual words and print the result of the split.')
taxa.split(',')
print(taxa.split(','))

print('\n-Store the result of split in a new variable named species')
species = taxa.split(',')

print('\n-Print species')
print(species)

print('\n-Print the species[1]. What do you get?')
print('Printing species[1], we get', species[1])

print('\n-Print type(species). What is its type?')
print('Its type is', type(species))

print('\n-Sort the list alphabetically and print.')
print(sorted(species, key=None, reverse=False))

print('\n-Sort the list by length of each string and print (the shortest string should be first).')
print(sorted(species, key=len))

print('\n')

print('\n3. Using the python interpreter, interrogate the difference between these two ways to copy a list. Careful! One of these is NOT what you might expect.')
print('\nMethod 1: \n-Create a list \n-Make a copy using the = assignment operator \n-Print the original list \n-Alter the list_copy by adding a new element using append() \n-Print the original list again')
lista = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
copia_lista = lista
print(lista)
copia_lista.append('sabingo')
print(lista)

print('\nMethod 2: \n-Create a list \n-Make a copy with the copy() method \n-Print the original list \n-Alther the list copy by adding a new element using append() \n-Print the original list again')
lista2 = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
copia_lista2 = lista2.copy()
print(lista2)
copia_lista2.append('Junho')
print(lista2)

print('\n')

print('\n4. Write a script that uses a while loop to print out the numbers 1 to 100.')
contagem = 0
while contagem < 101:
    print(contagem)
    contagem+=1

print('\n')

print('\n5. Write a script that uses a while loop to calculate the factorial of 1000')
numero = 1000
resultado=1
count=1
while count <= numero:
    resultado *= count
    count += 1
print(resultado)

print('\n')

print('\n6. Iterate through each element on this list using a for loop: [100,2,15,22,95,33,2,27,72,15,52]',
        '\n-Print out only the values that are even')
my_list = [100, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
for number in my_list:
    if x 
