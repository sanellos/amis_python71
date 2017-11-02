# --------
"""
Умова: Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. Визначити,
чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з
яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої.
рограма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

# Ввід координат початкової точки
x1 = int(input())
y1 = int(input())
# Ввід координат кінцевої точки
x2 = int(input())
y2 = int(input())
# Перевірка на можливість ходу
if (x1 == x2) or (y1 == y2):
    print("YES")
else:
    print("NO")
