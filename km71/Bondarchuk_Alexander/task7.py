# ------
"""
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. Користувач вводить чотири
цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини,
останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

# Запис перших координат
x1 = int(input())
y1 = int(input())
# Запис других координат
x2 = int(input())
y2 = int(input())
# Якщо остача від ділення однакова то клітинки одного кольору
if ((x1 - x2)%2==(y1-y2)%2):
    print("YES")
else:
    print("NO")

