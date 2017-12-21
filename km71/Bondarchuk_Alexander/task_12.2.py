def Max(list): #Шукаємо максимальне значення
    global largest
    if len(list) == 1:
        return list[0]
    else:
        largest = max(int(Max(list[:-1])), int(list[-1]))
        return largest


def count(list): #Знаходимо однакову к-сть
	Max(list)
	return list.count(str(largest))


print(count(input().split()))
