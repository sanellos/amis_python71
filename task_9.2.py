def power(a, n): # створюємо функцію
    result=1 # створюємо змінну
    count=1
    while(count<=n): # створюємо цикл
        result=result*a # збільшуємо результат на а
        count=count+1
    return result # повертаємо результат
a=float(input()) # ввід чисел
n=int(input())
result=power(a, n) # викликаємо функцію
print(result) # вивід відповіді
