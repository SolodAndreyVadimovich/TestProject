import operator
from typing import Callable

OPERATORS: dict[str, Callable[[any, any], bool]] = {
    "=": operator.eq,
    ">": operator.gt,
    "<": operator.lt,
}

def parse_condition(condition: str) -> tuple[str, str, str]:
    for op in OPERATORS:
        if op in condition:
            column, value = condition.split(op, 1)
            return column.strip(), op, value.strip()
    raise ValueError(f"Invalid filter condition: {condition}")

def convert(value: str) -> any:
    """Пытаемся преобразовать строку в int или float, иначе оставляем строкой."""
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value

def apply_filter(rows: list[dict], condition: str) -> list[dict]:
    column, op_symbol, raw_value = parse_condition(condition)
    comp = OPERATORS[op_symbol]
    target_value = convert(raw_value)

    result = []
    for row in rows:
        row_value = convert(row[column])
        if comp(row_value, target_value):
            result.append(row)

    return result
