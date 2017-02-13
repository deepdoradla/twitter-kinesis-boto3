#!/usr/bin/python


import time


def callTimeFunction(num):
        print('Printing this now, I will print this again after ' + str(num) + ' th second')


for i in range(30):
	callTimeFunction(i)
	time.sleep(1)

