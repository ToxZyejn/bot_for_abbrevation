import json
import pandas as pd

# Считываем таблицу из файла Excel в pandas DataFrame
df = pd.read_excel('abbreviaturs.xlsx')

# Проверяем, что в таблице 2 столбца
if df.shape[1] != 2:
    print('Ошибка: таблица должна содержать ровно 2 столбца')
    exit()

# Преобразуем данные в словарь
data = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))

# Конвертируем словарь в JSON
json_data = json.dumps(data, ensure_ascii=False)

# Выводим JSON в консоль или сохраняем в файл
print(json_data)
with open('abbreviaturka.json', 'w', encoding='utf-8') as file:
    file.write(json_data)



