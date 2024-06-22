def sum(x):
    return x+10
result = lambda x = 10 : x + 10
print(result())

# x = lambda a, b : a * b
# print(x(5, 6))

def twice(n):
    return lambda a : a * n
x = twice(2)
y = x(3)
print(y)

# write a quadratic equation using lambda
# When not to use lambda
# Write a program to fectch record form login db
# Write a python program to filter a list and extract only those
# words which starts from "c"

# pencil -
#
# when
# i
# start
# writing
# then
# after
# a
# sentence
# wrote
# i
# found
# it
# broken
#
# description: User is not able
# to
# write
# using
# pencil
#
# environment: Exam
# prerequisite:
# Pencil
# should
# be
# well
# preapared
# using
# sharpner
# User
# should
# have
# valid
# pencil
# User
# should
# write
# on
# valid
# notepad
#
# Steps1
# Take
# the
# give
# pencil and notepad
# Start
# writing
# after
# writing
# some
# some
# words
# observe
# the
# result
# actual:
# Pencil is breaking in middle
# of
# writing
#
# expected:
# user
# should
# be
# able
# to
# wirte
# without
# breakage
# while during writing
#
# what is working: user is able
# to
# write
# some
# words
# what is not working: pencil is breaking
# during
# writing
#
# attachment
# screenshot
# logs if any
#
# severioty - criticle