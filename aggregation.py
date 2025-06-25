from typing import Callable
import statistics

AGGREGATIONS: dict[str, Callable[[list[float]], float]] = {
    "avg": statistics.mean,
    "min": min,
    "max": max,
}


def parse_aggregation(agg: str) -> tuple[str, str]:
    if "=" not in agg:
        raise ValueError(f"Invalid aggregation: {agg}")
    column, op = agg.split("=", 1)
    return column.strip(), op.strip()


def apply_aggregation(rows: list[dict], agg: str) -> dict:
    column, op = parse_aggregation(agg)
    if op not in AGGREGATIONS:
        raise ValueError(f"Unsupported aggregation: {op}")

    try:
        values = [float(row[column]) for row in rows]
    except KeyError:
        raise ValueError(f"Column '{column}' not found in data.")
    except ValueError:
        raise ValueError(f"Column '{column}' must contain numeric values for aggregation.")

    result_value = AGGREGATIONS[op](values)
    return {f"{column}_{op}": result_value}
