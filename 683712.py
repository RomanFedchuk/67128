result = []

def divider(a, b):
    if a < b:
        raise ValueError("Значення 'a' не може бути меншим за 'b'")
    if b > 100:
        raise IndexError("Значення 'b' не може бути більшим за 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  # Видалено некоректний ключ []

for key in data:
    try:
        a = int(key)  # Перетворення ключа на ціле число (якщо це можливо)
        b = data[key]
        res = divider(a, b)
        result.append(res)
    except ZeroDivisionError:
        print(f"Помилка: Ділення на нуль для ключа {key} і значення {data[key]}")
    except ValueError as ve:
        print(f"ValueError: {ve} для ключа {key} і значення {data[key]}")
    except IndexError as ie:
        print(f"IndexError: {ie} для ключа {key} і значення {data[key]}")
    except TypeError as te:
        print(f"TypeError: {te} для ключа {key} і значення {data[key]}")
    except Exception as e:
        print(f"Невідома помилка: {e} для ключа {key} і значення {data[key]}")

print("Результат:", result)