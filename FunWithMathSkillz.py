# We are going to look at approximations of Pi
# as well as looking at the math Module

print(22 / 7)
print(355 / 113)

import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# See the loop above.  In addition to the value of pi, print the difference
#  between the values calculated by the archimedes function and by math.pi.
#  How many sides does it take to make the two close?


# Accumulators

acc = 0
for val in range(1, 6, 3):
    acc = acc + val

print(acc)


# Compute the sum of the first 100 even numbers
# Compute the sum of the first 50 odd numbers
# Compute the average of the first 100 odd numbers
# Write a function that returns the average of the first N numbers, where
#   N is a parameter
# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1.  Compute the 10th
#   Fibonacci number.
# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3.


# A Monte Carlo Simulation

# random numbers

import random

print(random.random())

# Boolean Expressions
# <, <=, >, >=, ==, !=
# Compound Boolean expressions
# and, or, not

dogWeight = 25
print(dogWeight < 25)
catWeight = 12
print(dogWeight > 25 or catWeight <= 10)
print(not catWeight <= 10)

# Decision making skills

alice = 20
bob = 15
carol = 25
ans = 0
if alice > 20:
    if bob < 50:
        ans = 150
    else:
        ans = 300
else:
    if carol > 500:
        ans = 200
    else:
        ans = 75
print(ans)

value = 75
if value > 100:
    print("bigger than 100")
elif value > 80:
    print("bigger than 80")
elif value > 45:
    print("bigger than 45")
else:
    print("not bigger than much")


def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

