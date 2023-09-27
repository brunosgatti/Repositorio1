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


