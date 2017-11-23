def distance(x1, y1, x2, y2): # створюється фунцію
    answer=((x1-x2)**2+(y1-y2)**2)**0.5 # блок обчилення
    return answer # повертається результат
x1=int(input()) # ввід данних
y1=int(input())
x2=int(input())
y2=int(input())
result=distance(x1, y1, x2, y2) # викликаємо функцію
print(result) # вивід відповіді
