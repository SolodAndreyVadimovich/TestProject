import argparse
import csv
from tabulate import tabulate


# Читаем CSV-файл и возвращаем список словарей
def read_csv(file_path):
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


# Пробуем преобразовать значение в число, иначе оставляем строкой
def convert(value):
    try:
        return float(value) if '.' in value else int(value)
    except ValueError:
        return value


# Фильтрация данных по условию: column>value, column<value, column=value
def filter_data(rows, condition):
    if ">" in condition:
        column, value = condition.split(">")
        op = ">"
    elif "<" in condition:
        column, value = condition.split("<")
        op = "<"
    elif "=" in condition:
        column, value = condition.split("=")
        op = "="
    else:
        raise ValueError("Неправильное условие фильтрации")

    column, value = column.strip(), value.strip()
    value = convert(value)

    result = []
    for row in rows:
        cell = convert(row[column])
        if op == ">" and cell > value:
            result.append(row)
        elif op == "<" and cell < value:
            result.append(row)
        elif op == "=" and cell == value:
            result.append(row)
    return result


# Выполнение агрегации (avg, min, max) по числовому столбцу
def aggregate_data(rows, arg):
    column, operation = arg.split("=")
    column = column.strip()
    operation = operation.strip()

    try:
        values = [float(row[column]) for row in rows]
    except ValueError:
        raise ValueError("Агрегация доступна только для числовых колонок")

    if operation == "avg":
        result = sum(values) / len(values)
    elif operation == "min":
        result = min(values)
    elif operation == "max":
        result = max(values)
    else:
        raise ValueError("Допустимы только операции: avg, min, max")

    return {f"{column}_{operation}": result}


# Основная логика: разбираем аргументы, читаем файл, применяем фильтр или агрегацию
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Путь к CSV-файлу")
    parser.add_argument("--where", help="Фильтр, например: price>500")
    parser.add_argument("--aggregate", help="Агрегация, например: price=avg")
    args = parser.parse_args()

    rows = read_csv(args.file_path)

    if args.where:
        rows = filter_data(rows, args.where)
        print(tabulate(rows, headers="keys"))
    elif args.aggregate:
        result = aggregate_data(rows, args.aggregate)
        print(result)
    else:
        print(tabulate(rows, headers="keys"))


if __name__ == "__main__":
    main()
