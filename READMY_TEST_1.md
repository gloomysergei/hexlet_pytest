## tests/test_generate_password.py

В этом упражнении вам предстоит написать тесты для функции генерации паролей `generate_password(length, include_uppercase, include_digits, include_special)`.

Функция принимает следующие аргументы:

- `length` – длина пароля, по умолчанию 5 символов
- `include_uppercase` – включать ли заглавные буквы, `False` по умолчанию
- `include_digits` – включать ли цифры, `False` по умолчанию
- `include_special` – включать ли специальные символы `[!@#$%^&*(),.?":{}|<>]`, `False` по умолчанию

Так функция выглядит в коде:

```python
generate_password() # asdfg
generate_password(5, include_uppercase=True) # tYRop
generate_password(5, include_uppercase=True, include_digits=True) # 3hGJ2
generate_password(5, include_uppercase=True, include_digits=True, include_special=True) # 8I]io
```

Функция гарантирует, что будем использован как минимум один из символов указаного типа.

### src/solution.py

Реализуйте функцию `generate_password(length, include_uppercase, include_digits, include_special)`, основываясь на описании и примерах ее работы.

### Подсказки

- Один из тестов уже написан в упражнении. Используйте его как образец при написании своих тестов.
- Используйте пакет `string` для наборов символов
- Для проверки на вхождение символов можно использовать как и простое `in`, так и регулярные выражения
