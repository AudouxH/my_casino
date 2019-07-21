#!/usr/bin/python
from random import randrange
import time

play_again = True

print 'Hello ! And welcome to my_casino the game.'

choise = -1
while choise < 1 or choise > 2 :
    choise = input ('do you want see roles or begining game ?\n1 = roles    2 = playing\nyour choise : ')
    try:
        choise = int(choise)
    except ValueError:
        print("you haven't take good number.")
        choise = -1
        continue

if choise == 1 :
    print '\nThe goal is quite simple in itself but relies on a lot of luck.'
    print 'You will have to choose a number between 0 and 49 that will be present around the roulette wheel.'
    print 'You will then put the sum that you want on the figure you have chosen.'
    print 'The roulette will then turn, nothing goes! and a ball will then fall on a number between 0 and 49.'
    print 'If your chosen number is the same as that of the roulette then carry 3 times your bet.'
    print "If your number is the same color as that of the roulette wheel, that is to say that both are self or even all the imperial,"
    print 'you will only lose half of your stake.'
    print 'To finish if the two figures we have nothing in common you lose your bet.\n'
    been = raw_input ("Do you want to start playing ? (yes) : ")
elif choise == 2 :
    print "\nGreat let's go !!"

print "welcome on the table, you're right on time, we'll can begining.\n\n"
print 'Choose how much money want you start : \n'
print '1 = 500$\n2 = 1000$\n3 = 1500$\n4 = 2000$\n'


choise_2 = -1
while choise_2 < 1 or choise_2 > 4 :
    choise_2 = input ('your choice : ')
    try:
        choise_2 = int(choise_2)
    except ValueError:
        print("you haven't take good number")
        choise_2 = -1
        continue

if choise_2 == 1 :
    cash = 500
elif choise_2 == 2 :
    cash = 1000
elif choise_2 == 3 :
    cash = 1500
else :
    cash = 2000
print 'You have choice to begin with', cash, "$\nAlright let's go !\n"

while play_again :
    nb_choise = -1
    while nb_choise < 0 or nb_choise > 49 :
        nb_choise = input ("It's you to choose the number on which you want bet between 0 and 49 included: ")
        try:
            nb_choise = int(nb_choise)
        except ValueError:
            print("you haven't take good number")
            nb_choise = -1
            continue

    nb_random = randrange(0, 50)

    mise = -1
    while mise < 1 or mise > cash :
        mise = input ("Alright, how much do you bet on this number: ")
        try:
            mise = int(mise)
        except ValueError:
            print("you haven't take good number")
            mise = -1
            continue

    print 'The roulette wheel ...'

    time.sleep(2)
    print "\n...and stop on number", nb_random
    if nb_random == nb_choise :
        print 'Well done you have found good number\n'
        cash = cash + (3 * mise)
    elif (nb_choise % 2) == (nb_random % 2) :
        print "Pity you haven't found good number but you have same color\n"
        cash = cash - (mise / 2)
    else :
        print 'You have lost, pity\n'
        cash = cash - mise
    print "You still have", cash, '$'

    if cash < 1 :
        print "You are dry, you must get out of the table... See you soon!"
        play_again = False
    else :
        again = raw_input('Do you want replay ? (y/n): ')
        if again == "n" or again == "N" :
            print "Thanks to play at roulette ! you go out with", cash, '$'
            play_again = False
        elif again == "y" or again == "Y":
            print 'Great continue\n'
