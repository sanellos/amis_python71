def power(a, n):
    if n == 0: # початкове значення, якщо n уже дорівнює 0
        return 1
    else: # підрахунок степення в іншому випадку
        return a * power(a, n - 1)
a=float(input()) # ввід чисел
n=int(input())
print(power(a, n)) # вивід відповіді
