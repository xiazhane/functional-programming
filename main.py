# Главная функция, демонстрирующая использование функций из модуля
def main():
    # Получаем значения с клавиатуры
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))

    # Примеры использования функций из модуля functions
    result_add = add(x, y)
    print("Сложение:", result_add)

    result_subtract = subtract(x, y)
    print("Вычитание:", result_subtract)

    result_multiply = multiply(x, y)
    print("Умножение:", result_multiply)

    result_divide = divide(x, y)
    print("Деление:", result_divide)

if "__main__" == name:
    main()