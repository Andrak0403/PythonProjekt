#!/usr/bin/python3

answer = input('Is your dog hungry? yes/no: ')

if answer.lower() == 'yes':
   print(f'Your answer is {answer}, feed the dog!')
elif answer.lower() == 'no':
   print(f'Your answer is {answer}, the dog will starve!')
else:
   print('Answer not recognized, program terminating')
print('***Program complete***')
