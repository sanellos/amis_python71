# ---------
"""
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

The next number for the number 179 is 180.
The previous number for the number 179 is 178.

Вхідні дані: ціле число

Вихідні дані: два рядки за наведеним у завдання форматом.
"""

number = int(input())
print("The next number for the number ", number, " is ", number + 1, ".", sep="")
print("The previous number for the number ", number, " is ", number - 1, ".", sep="")