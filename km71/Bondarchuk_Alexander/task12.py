# -------
"""
Умова: Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений на дві частини тільки
по горизонталі або по вертикалі, при цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один
крок таким чином, щоб одна з частин матиме точно k клітин. Програма має вивести "YES", якщо шоколад можна поділити,
або "NO" в іншому випадку.

Вхідні дані: 3 цілих числа: n,m, k. Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

# Шоколадка розміром n на m
n = int(input())
m = int(input())
# Площу неохыдної частини
k = int(input())
# Перевірка
if (k % n == 0) and (k < n * m):
    print("YES")
elif (k % m == 0) and (k < n * m):
    print("YES")
else:
    print("NO")
