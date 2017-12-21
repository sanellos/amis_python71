def Max(list): #Шукаємо максимальне значення
    global largest
    if len(list) == 1:
        return list[0]
    else:
        largest = max(int(Max(list[:-1])), int(list[-1]))
        return largest


def Max2(list):
	Max(list)
	list.remove(str(largest)) #Видаляємо 1 максимальний елемент
	Max(list) #Шукаємо 2 максимальний елемент
	return(str(largest))


print(Max2(input().split()))
