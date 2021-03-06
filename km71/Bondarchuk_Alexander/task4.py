# ---------
"""
N кеглів виставили в один ряд, занумерованих їх зліва направо числами від 1 до N. Потім з цього ряду кинули K куль,
при цьому i-й куля збив всі кеглі з номерами від li до ri включно. Визначте, які кеглі залишилися стояти на місці.

Програма отримує на вхід кількість кеглів N і кількість кидків K. Далі йде K пар чисел li, ri, при цьому 1≤ li≤ ri≤ N.

Програма повинна вивести послідовність з N символів, де j-й символ є "I", якщо j-я кегля залишилася стояти, або ".",
Якщо j-я кегля була збита.
"""

n, k = [int(i) for i in input().split()] #вводимо дані
a = [1 for i in range(n)] #заповнюємо список 1 (кеглі стоять)
for i in range(k):
    x, y = [int(i) for i in input().split()] #замінємо всі елементи як належать діапозону на 0 (кеглі впали)
    for i in range(x-1, y): #віднімаємо 1, оскільки індексація з 0
        if a[i] == 1:
            a[i] = 0
for i in a:
    if i == 1:
        print('|', end='') #виводимо дані
    else:
        print('.', end='') #виводимо дані
input()
