from pathlib import Path

config_path = Path(__file__)
current_dir = Path.cwd()
home_dir = Path.home()

print(f"Путь к конфигу: {config_path}")
print(f"Текущая директория: {current_dir}")
print(f"Домашняя директория: {home_dir}")

root_path = Path('/src')
full_path = root_path / 'stack' / 'sergey.conf'
print(full_path)
