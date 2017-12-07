def reverse(list): #створюємо ф-цію
    if len(list) == 0: #умова не виконання блоку ф-ції
        return '' #повертаємо пробіл
    return str(list[-1]) + ' ' + reverse(list[:-1]) #повертаємо обернений список


list = [i for i in input().split()] #створюємо список з чисел
print(reverse(list))  #вивід результату
