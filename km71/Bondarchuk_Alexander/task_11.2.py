def check_min(list): #створюємо ф-цію
    if len(list) != 1: #умова виконання ф-ції
        if list[0] >= list[1]: #перевіряємо перші 2 елементи
            return check_min(list[1:]) #повертаємо функцію для порівняння наступних чисел
        else:
            del list[1] #видаляє другий елемент в списку
            return check_min(list) #вовертаємо функцію
    else: #умова не виконання блоку ф-ції і вивід єдиного елементу
        return list[0] #повертаємо єдиний елемент


list = [float(i) for i in input().split()] #створюємо список з чисел
print(check_min(list)) #вивід результату
