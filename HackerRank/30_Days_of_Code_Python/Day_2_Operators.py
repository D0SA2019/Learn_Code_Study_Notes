# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
,

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = float(meal_cost * (tip_percent / 100))
    tax = float(meal_cost * (tax_percent / 100))
    totalCost = float(meal_cost) + tip + tax
    print(round(totalCost))

if __name__ == '__main__':
    meal_cost = float(input("Input the meal cost: "))

    tip_percent = int(input("Input the tip percent: "))

    tax_percent = int(input("Input the tax percent: "))

    solve(meal_cost, tip_percent, tax_percent)
