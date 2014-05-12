from __future__ import print_function
import math


TAX = 0.08875
GRATUITY = 0.25


def you_owe(menu, meal):
    food = 0
    for m in meal:
        if m in menu:
            food += meal[m] * menu[m]
    tax = food * TAX
    gratuity = (food + tax) * GRATUITY
    total = food + tax + gratuity
    return math.floor(100 * total) / 100


if __name__ == '__main__':
    menu1 = {"calamari":5, "carbonara":15, "branzino":15, "cheesecake":7.50}
    meal1 = {"calamari":1, "carbonara":1, "branzino":1, "cheesecake":2}
    menu2 = {"a": 4.5, "b": 3.4, "c": 9}
    meal2 = {"a": 1, "b": 5}
    print(you_owe(menu1, meal1))
    print(you_owe(menu2, meal2))
