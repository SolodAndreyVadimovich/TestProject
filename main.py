import argparse
from csv_reader import read_csv
from filters import apply_filter
from aggregation import apply_aggregation
from tabulate import tabulate


def parse_args():
    parser = argparse.ArgumentParser(description="CSV Processor")
    parser.add_argument("file_path", help="Path to the CSV file")
    parser.add_argument("--where", help="Filter condition, e.g. 'price>500'")
    parser.add_argument("--aggregate", help="Aggregation condition, e.g. 'price=avg'")
    return parser.parse_args()


def main():
    args = parse_args()
    rows = read_csv(args.file_path)

    if args.where:
        rows = apply_filter(rows, args.where)
        print(tabulate(rows, headers="keys"))
    elif args.aggregate:
        result = apply_aggregation(rows, args.aggregate)
        print(result)
    else:
        print(tabulate(rows, headers="keys"))


if __name__ == "__main__":
    main()
