def check_i(i):
    try: # перевіряємо чи дані введені правильно
        i = int(i)
        if i > 0:
            k = True
        else:
            k = False
    except:
        k = False
    return k


def check_x(x):
    try: # перевіряємо чи дані введені правильно
        x = float(x)
        if x!=0:
            return True
        else:
            return False
    except:
        return False



def sumFunc(x, i): # обчислення суми
    if i==0:
        return 1/x
    return ((x+1)/x**2)+sumFunc(x, i-1)

def run(): # перевіряємо
    i = input()
    x = input()
    print(check_i(i))
    print(check_x(x))
    if check_i(i)==check_x(x)==True:# Перевіряємо чи перші 2 функції правильні
        print(sumFunc(x, i))
    else:
        print("False")
