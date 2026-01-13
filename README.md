# Фреймворк Pytest

## Настройка и запуск

1. создаем директорию `hexlet_pytest`. Заходим в нее и выполняем команды

```bash
uv init
mkdir tests
```

2. Устанавливаем пакет используя команду `uv add --dev pytest`
3. Устанавливаем в `pyproject.toml` блок:

```python
[build-system]
requires = ['hatchling']
build-backend = 'hatchling.build'

[tool.hatch.build.targets.wheel]
packages = ['hexlet_pytest']
```

### Пояснения

`[build-system]`
Раздел, описывающий систему сборки проекта (соответствует стандартам PEP 517 и PEP 660).

`requires` [перевод](https://www.reverso.net/text-translation#sl=eng&tl=rus&text=requires)
Список пакетов, которые должны быть установлены до начала сборки проекта. В данном случае нужен только `hatchling`[перевод](https://www.reverso.net/text-translation#sl=eng&tl=rus&text=hatchling)

`build-backend`
Указывает, какой именно бэкенд (движок сборки) использовать. Здесь: `hatchling.build` — стандартный бэкенд от `hatchling`.

Это фрагмент конфигурации для инструмента Hatch (современная система сборки Python‑пакетов), заданный в файле pyproject.toml.

### Разбор секции tool

```python
[tool.hatch.build.targets.wheel]
packages = ['hexlet_pytest']
```

`[tool.hatch.build.targets.wheel]`

Это раздел конфигурации, который определяет параметры сборки `wheel‑пакета`(стандартный формат дистрибутива Python).

`tool.hatch` — корень настроек для Hatch.

`build.targets.wheel` — конкретная цель сборки `(wheel)`.

`packages = ['hexlet_pytest']` - указывает, какие пакеты Python должны быть включены в итоговый wheel.

`hexlet_pytest` — имя пакета (должно соответствовать директории с __init__.py в проекте).

Если в проекте несколько пакетов, их перечисляют через запятую:

```bash
toml
packages = ['package1', 'package2']
```

### Зачем это нужно

- Контроль содержимого `wheel`. `Hatch` будет включать в дистрибутив только указанные пакеты (и их подпакеты/модули).

- Избегание лишних файлов. Без явного указания packages `Hatch` может включить нежелательные директории (например, тесты или документацию).

- Гибкость. Можно собирать только часть проекта, если он содержит несколько логически независимых пакетов.

### Где располагается

В файле `pyproject.toml` полный блок может выглядеть так:

```bash
toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build]
# Общие настройки сборки

[tool.hatch.build.targets.wheel]
packages = ['hexlet_pytest']
exclude = [
  "/tests",
  "/docs",
]
```

### Дополнительные параметры (опционально)

В секции `[tool.hatch.build.targets.wheel]` можно указать:

- `exclude` — список шаблонов для исключения файлов/директорий:

```bash
toml
exclude = ["/tests", "/scripts", "*.pyc"]
```

- `include` — явное включение файлов (перекрывает `exclude`):

```bash
toml
include = ["/src/hexlet_pytest/data/*.json"]
```

- `python-tag` — указание версии Python (например, "py37").

- `abi-tag` — ABI‑тег для расширений C (редко используется).

### Как проверить сборку

- Установите Hatch:

```bash
bash
pip install hatchling
```

- Соберите `wheel`:

```bash
bash
hatch build
```

- Проверьте содержимое:

```bash
bash
unzip -l dist/hexlet_pytest-*.whl
```

### Итог:

строка `packages = ['hexlet_pytest']` говорит `Hatch`, что в wheel‑дистрибутив нужно включить только пакет `hexlet_pytest` из вашего проекта. Это помогает контролировать состав итогового пакета и избегать избыточности.
