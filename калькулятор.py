history = []
print("калькулятор")
mode = input("выберите режим (1 - обычный, 2 - цепочка): ")
while mode != "1" and mode != "2":
    print("Ввод неверный!")
    mode = input("выберите режим (1 - обычный, 2 - цепочка): ")

while True:
    command = input("Введите команду или число: ").strip().lower()

    if command == "exit" or command == "quit":
        print("Гуд бай")
        break
    elif command == "history":
        if not history:
            print("История пуста")
        else:
            print("История операций")
            for item in history:
                print(item)

    elif command == "clear":
        history.clear()
        print("История очищена")
    else:
        try:
            if mode == "1":
                num1 = float(input("Введите первое число: "))
                operator = input("Введите оператор: ")
                num2 = float(input("Введите второе число: "))
            elif mode == "2":
                if 'current_result' not in locals():
                    num1 = float(input("Введите первое число: "))
                else:
                    num1 = current_result
                    print(f"Текущее число: {num1}")
                operator = input("Введите оператор: ")
                num2 = float(input("Введите второе число: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            elif operator == "**":
                result = num1 ** num2
            elif operator == "//":
                result = num1 // num2
            elif operator == "%":
                result = num1 % num2
            else:
                print("Неизвестный оператор")
                continue
            current_result = result
            print(result)
            history.append(f"{num1} {operator} {num2} = {result}")

        except ValueError:
            print("Ошибка: нужно вводить числа!")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль!")




    
