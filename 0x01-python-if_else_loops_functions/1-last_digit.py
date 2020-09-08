#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
=======

>>>>>>> 43fcea7d944bd092fe5abea30255a1221c74091b
if (number < 0):
    print('Last digit of {:d} '
          'is {:d} and is less than 6 and not 0'
          .format(number, -(-number % 10)))

elif number % 10 > 5:
    print('Last digit of {:d} '
          'is {:d} and is greater than 5'.format(number, number % 10))
elif number % 10 == 0:
    print('Last digit of {:d} '
          'is 0 and is 0'.format(number))
else:
    print('Last digit of {:d} '
          'is {:d} and is less than 6 and not 0'.format(number, number % 10))
<<<<<<< HEAD
l = int(repr(number)[-1]
    if (l > 5):
        print("Last digit of {:d} is {:d} and is greater than 5".format(number, l))
    if (l == 5):
        print("Last digit of {:d} is {:d} and is 0".format(number, l))
    if ((l < 6) and (number != 0)):
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, l))
    if (number>5)
        print ("and is greater than 5")
    if (number == 0)
        print ("and is 0)
    if (number < 6 )
        print ("and is less than 6 and not 0")
=======
    
>>>>>>> 43fcea7d944bd092fe5abea30255a1221c74091b
