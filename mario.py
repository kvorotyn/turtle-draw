#!/usr/bin/env python
from __future__ import print_function

import turtle as t

colors = {
	'body': '#ffc142',
	'eyes': 'black',
	'hair': '#472306',
	'moustache': 'black',
	'hat': 'red',
	'shirt': 'red',
	'pants': 'blue',
	'buttons': 'yellow',
	'boots': '#472306'
}
step = 30


def f(n):
	'''Move n steps forward.'''
	t.forward(n * step)


def b(n):
	'''Move n steps backward.'''
	t.backward(n * step)


def r(angle=90):
	'''Turn right by given angle.'''
	t.right(angle)


def l(angle=90):
	'''Turn left by given angle.'''
	t.left(angle)


def rectangle(a, b, clockwise=True):
	t.begin_fill()
	for i in range(2):
		f(a)
		r() if clockwise else l()
		f(b)
		r() if clockwise else l()
	t.end_fill()


def square(a, clockwise=True):
	rectangle(a, a, clockwise)


def half_body(right=True):
	start = t.pos()
	t.setheading(-90)  # look down
	t.down()
	t.color(colors['shirt'])
	rectangle(2, 1, not right)
	l() if right else r()
	f(1)
	t.color(colors['pants'])
	rectangle(1, 3, right)
	t.setheading(-90)
	f(2)
	rectangle(4, 1, right)
	f(1)
	t.color(colors['buttons'])
	square(1, not right)
	t.color(colors['pants'])
	f(1)
	rectangle(3, 2, not right)
	l() if right else r()
	f(1)
	square(1, not right)
	t.setheading(90)
	f(1)

	# Sleeve.
	t.color(colors['shirt'])
	t.begin_fill()
	f(3)
	r() if right else l()
	f(1)
	for i in range(3):
		f(1)
		t.setheading(-90)
		f(1)
		l() if right else r()
	r(180)
	f(2)
	t.setheading(-90)
	f(1)
	r() if right else l()
	f(1)
	t.setheading(90)
	f(1)
	l() if right else r()
	f(1)
	t.end_fill()

	# Hand.
	b(2)
	r(180)
	t.color(colors['body'])
	rectangle(2, 3, right)
	t.setheading(-90)
	f(1)
	square(1, right)
	f(1)

	t.color(colors['pants'])
	rectangle(2, 1, right)
	f(2)
	
	t.color(colors['boots'])
	l() if right else r()
	f(1)
	t.setheading(-90)
	rectangle(2, 3, right)
	f(1)
	square(1, not right)
	
	t.up()
	t.goto(start)


t.up()
t.goto(-100, 250)
t.down()

t.speed(0)

# Hat.
t.color(colors['hat'])
t.begin_fill()
f(5)
r()
f(1)
l()
f(3)
r()
f(1)
r()
f(9)
r()
f(1)
r()
f(1)
l()
f(1)
t.end_fill()

# Hair.
t.up()
b(2)
r()
t.down()
t.color(colors['hair'])
t.begin_fill()
f(2)
r()
f(1)
r()
f(1)
l()
f(1)
l()
f(1)
r()
f(1)
r()
f(2)
r()
f(2)
l()
f(1)
r()
f(1)
r()
f(1)
t.end_fill()
b(1)
r()
f(1)
rectangle(2, 1)
f(2)
square(1, False)
l()

# Ear.
t.color(colors['body'])
rectangle(1, 2, False)

# Face.
f(1)
t.begin_fill()
f(2)
l()
f(1)
l()
f(1)
r()
f(1)
r()
f(1)
l()
f(1)
r()
f(2)
r()
f(2)
l()
f(1)
r()
f(1)
r()
f(1)
l()
f(1)
l()
f(2)
r()
f(1)
r()
f(6)
r()
f(2)
t.end_fill()
r()
f(5)
l()
f(1)

# Nose.
t.begin_fill()
f(2)
r()
f(1)
r()
f(1)
l()
f(2)
r()
f(1)
l()
f(1)
r()
f(1)
r()
f(3)
r()
f(1)
l()
f(1)
t.end_fill()

# Eye.
t.color(colors['eyes'])
rectangle(1, 2)
l()
# Moustache.
t.color(colors['moustache'])
square(1, False)
f(1)
square(1)
rectangle(1, 3, False)

# Move to the lower center of the neck.
t.up()
f(2)
r()
f(2)
l()

# Body.
half_body(True)
half_body(False)

t.hideturtle()
t.done()