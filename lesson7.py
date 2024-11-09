#Lesson7
# Ітератори - це поведінковий патерн, що дозволяє послідовно обходити складну колекцію, не розкриваючи деталі її реалізації.
#Замикання/декоратори - це

print('Lesson 7. Iterators, Decorators')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('before', numbers)

# for i in range(len(numbers)): Цикл в котором перменная и ид'т подсчет символлов
#     numbers[i] = numbers[i]**2 Переменную і подносят в квадрат
#
# print('after', numbers)

def up_square(n): #Функція котра відкидає значення кратні 2
    if n % 2 != 0:
        return n**2
    return n

def check_if_more(n): #Функція котра повертає Тruе або False якщо число більше 5
    if n >= 5:
        return True
    return False


numbers_square = [up_square(n) for n in numbers if check_if_more(n)]
print('after', numbers_square)

