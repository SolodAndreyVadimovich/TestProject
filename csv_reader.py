import csv

def read_csv(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
