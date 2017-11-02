# -------
"""
Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. Дано
координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два
числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в
іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

# координата початку
x1 = int(input("Enter a coordinate one: "))
y1 = int(input("Enter a coordinate two: "))
# Координата закінчення
x2 = int(input("Enter a coordinate three: "))
y2 = int(input("Enter a coordinate four: "))
# Перевірка можливості
if(((x1 == x2)&((y1 == y2-1)^(y1 == y2+1)))^((x1 == x2+1)&((y1 == y2-1)^(y1 == y2+1)^(y1 == y2)))^((x1 == x2-1)&((y1 == y2-1)^(y1 == y2+1)^(y1 == y2)))):
    answer = 'YES'
else:
    answer = 'NO'
print(answer)
