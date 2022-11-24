#import sys
#import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

distance = int(input())
time = int(input())
velocity = int(input())
fuel = int(input())
fuel_consumption = int(input())

if (velocity * time) < distance:
    print( "Failure, Not enough time")
elif (fuel * fuel_consumption) < distance:
    print("Failure, Not enough fuel")
elif ((velocity * time) < distance) or ((fuel * fuel_consumption) < distance):
    print("Failure, Not enough time")
elif ((velocity * time) < distance) and ((fuel * fuel_consumption) < distance):
    print("Welcome to Mars")
else: print("olmadı")