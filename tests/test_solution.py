from pathlib import Path

# функция, которую нужно протестировать
# to_html_list = get_function()


# BEGIN (write your solution here)
csv_path = Path('test_data/list.csv').resolve()
json_path = Path('test_data/list.json').resolve()
yaml_path = Path('test_data/list.yaml').resolve()
result_path = Path('test_data/result.html').resolve()
print(result_path) # получаем объект

read_content = json_path.read_text(encoding='utf8')
print(read_content)
# END
