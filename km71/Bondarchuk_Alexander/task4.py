# -----------
"""
Умова: N студентів отримали K яблук і розподілити їх між собою порівну.
Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент?
Скільки яблук залишиться в кошику?

Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на поставлені вище питання.

Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - кількість яблук, що лишилось у кошику.
"""
#Вводимо цілі числа
N=int(input())
K=int(input())
get=(K//N) #Яблук отримає кожен студент
basket=(K%N) #Яблук залишиться в кошику
print(get) #Вивід даних
print(basket)
